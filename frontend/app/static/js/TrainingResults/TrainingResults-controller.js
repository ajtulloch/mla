'use strict';

angular.module('app')
  .controller('TrainingResultsController', ['$scope', '$modal', 'resolvedTrainingResults', 'TrainingResults',
    function ($scope, $modal, resolvedTrainingResults, TrainingResults) {

      $scope.Trainingresults = resolvedTrainingResults;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.TrainingResults = TrainingResults.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        TrainingResults.delete({id: id},
          function () {
            $scope.Trainingresults = TrainingResults.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          TrainingResults.update({id: id}, $scope.TrainingResults,
            function () {
              $scope.Trainingresults = TrainingResults.query();
              $scope.clear();
            });
        } else {
          TrainingResults.save($scope.TrainingResults,
            function () {
              $scope.Trainingresults = TrainingResults.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.TrainingResults = {
          
          "jsonString": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var TrainingResultsSave = $modal.open({
          templateUrl: 'TrainingResults-save.html',
          controller: TrainingResultsSaveController,
          resolve: {
            TrainingResults: function () {
              return $scope.TrainingResults;
            }
          }
        });

        TrainingResultsSave.result.then(function (entity) {
          $scope.TrainingResults = entity;
          $scope.save(id);
        });
      };
    }]);

var TrainingResultsSaveController =
  function ($scope, $modalInstance, TrainingResults) {
    $scope.TrainingResults = TrainingResults;

    $scope.ok = function () {
      $modalInstance.close($scope.TrainingResults);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };

angular.module('app')
  .controller(
    'TrainingResultsCtrl',
    ['$scope', '$routeParams', 'TrainingResults', '$log',
     function($scope, $routeParams, TrainingResults, $log) {
       $scope.results = TrainingResults.get({id:$routeParams.reportId}, function() {
         _.map($scope.results.jsonReport.models, function(model) {
           model.performanceStatistics.lineRocCurve = [{
             "key": $scope.algorithmEnumToName[model.algorithm],
             "values": _.map(
               model.performanceStatistics.rocCurve,
               function(p) { return [p.falsePositiveRate, p.truePositiveRate] })
           }];
           $log.info(model.performanceStatistics.lineRocCurve);
         });
         
         $scope.results.jsonReport.rocCurves =
           _.chain($scope.results.jsonReport.models)
           .map(function(model) {
             return model.performanceStatistics.lineRocCurve[0];
           })
           .value();
         $log.info("Curves: ", $scope.results.jsonReport.rocCurves);
       });
       $log.info($scope.results);

       $scope.algorithmEnumToName = {
         1: 'Logistic Regression',
         2: 'Gradient Boosted Decision Trees',
         3: 'Random Forests',
         4: 'Linear SVM',
         5: 'Nonlinear SVM',
       }
       $scope.metricEnumToName = {
         1: 'Accuracy',
         2: 'Average Precision',
         3: 'f1',
         4: 'Log Loss',
         5: 'Precision',
         6: 'Recall',
         7: 'ROC AUC',
       };
     }
    ]
  )
  

