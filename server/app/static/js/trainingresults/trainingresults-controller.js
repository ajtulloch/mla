'use strict';

angular.module('mlserver')
  .controller('TrainingresultsController', ['$scope', '$modal', 'resolvedTrainingresults', 'Trainingresults',
    function ($scope, $modal, resolvedTrainingresults, Trainingresults) {

      $scope.trainingresults = resolvedTrainingresults;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.trainingresults = Trainingresults.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Trainingresults.delete({id: id},
          function () {
            $scope.trainingresults = Trainingresults.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Trainingresults.update({id: id}, $scope.trainingresults,
            function () {
              $scope.trainingresults = Trainingresults.query();
              $scope.clear();
            });
        } else {
          Trainingresults.save($scope.trainingresults,
            function () {
              $scope.trainingresults = Trainingresults.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.trainingresults = {
          
          "results": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var trainingresultsSave = $modal.open({
          templateUrl: 'trainingresults-save.html',
          controller: TrainingresultsSaveController,
          resolve: {
            trainingresults: function () {
              return $scope.trainingresults;
            }
          }
        });

        trainingresultsSave.result.then(function (entity) {
          $scope.trainingresults = entity;
          $scope.save(id);
        });
      };
    }]);

var TrainingresultsSaveController =
  function ($scope, $modalInstance, trainingresults) {
    $scope.trainingresults = trainingresults;

    

    $scope.ok = function () {
      $modalInstance.close($scope.trainingresults);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
