'use strict';

angular.module('mlserver')
  .controller('DatasetController', ['$scope', '$modal', 'resolvedDataset', 'Dataset',
    function ($scope, $modal, resolvedDataset, Dataset) {

      $scope.datasets = resolvedDataset;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.dataset = Dataset.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Dataset.delete({id: id},
          function () {
            $scope.datasets = Dataset.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Dataset.update({id: id}, $scope.dataset,
            function () {
              $scope.datasets = Dataset.query();
              $scope.clear();
            });
        } else {
          Dataset.save($scope.dataset,
            function () {
              $scope.datasets = Dataset.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.dataset = {
          
          "name": "",
          
          "examples": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var datasetSave = $modal.open({
          templateUrl: 'dataset-save.html',
          controller: DatasetSaveController,
          resolve: {
            dataset: function () {
              return $scope.dataset;
            }
          }
        });

        datasetSave.result.then(function (entity) {
          $scope.dataset = entity;
          $scope.save(id);
        });
      };
    }]);

var DatasetSaveController =
  function ($scope, $modalInstance, dataset) {
    $scope.dataset = dataset;

    

    $scope.ok = function () {
      $modalInstance.close($scope.dataset);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
