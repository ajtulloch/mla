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
       $scope.report = TrainingResults.get({id:$routeParams.reportId}, function() {
         $scope.report.json = angular.fromJson($scope.report.jsonString);
         $scope.report.summary = {
           numSamples: 100,
           numPositives: 80,
           numNegatives: 50,
         };
       });
       $log.debug($scope.report);
     }
    ]
  )

