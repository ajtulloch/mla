'use strict';

angular.module('app')
  .controller('BatchTrainingRequestController', ['$scope', '$modal', 'resolvedBatchTrainingRequest', 'BatchTrainingRequest',
    function ($scope, $modal, resolvedBatchTrainingRequest, BatchTrainingRequest) {

      $scope.Batchtrainingrequests = resolvedBatchTrainingRequest;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.BatchTrainingRequest = BatchTrainingRequest.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        BatchTrainingRequest.delete({id: id},
          function () {
            $scope.Batchtrainingrequests = BatchTrainingRequest.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          BatchTrainingRequest.update({id: id}, $scope.BatchTrainingRequest,
            function () {
              $scope.Batchtrainingrequests = BatchTrainingRequest.query();
              $scope.clear();
            });
        } else {
          BatchTrainingRequest.save($scope.BatchTrainingRequest,
            function () {
              $scope.Batchtrainingrequests = BatchTrainingRequest.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.BatchTrainingRequest = {
          
          "trainingData": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var BatchTrainingRequestSave = $modal.open({
          templateUrl: 'BatchTrainingRequest-save.html',
          controller: BatchTrainingRequestSaveController,
          resolve: {
            BatchTrainingRequest: function () {
              return $scope.BatchTrainingRequest;
            }
          }
        });

        BatchTrainingRequestSave.result.then(function (entity) {
          $scope.BatchTrainingRequest = entity;
          $scope.save(id);
        });
      };
    }]);

var BatchTrainingRequestSaveController =
  function ($scope, $modalInstance, BatchTrainingRequest) {
    $scope.BatchTrainingRequest = BatchTrainingRequest;

    

    $scope.ok = function () {
      $modalInstance.close($scope.BatchTrainingRequest);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
