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
