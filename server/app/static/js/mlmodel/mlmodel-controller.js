'use strict';

angular.module('mlserver')
  .controller('MlmodelController', ['$scope', '$modal', 'resolvedMlmodel', 'Mlmodel',
    function ($scope, $modal, resolvedMlmodel, Mlmodel) {

      $scope.mlmodels = resolvedMlmodel;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.mlmodel = Mlmodel.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Mlmodel.delete({id: id},
          function () {
            $scope.mlmodels = Mlmodel.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Mlmodel.update({id: id}, $scope.mlmodel,
            function () {
              $scope.mlmodels = Mlmodel.query();
              $scope.clear();
            });
        } else {
          Mlmodel.save($scope.mlmodel,
            function () {
              $scope.mlmodels = Mlmodel.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.mlmodel = {
          
          "name": "",
          
          "serialized": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var mlmodelSave = $modal.open({
          templateUrl: 'mlmodel-save.html',
          controller: MlmodelSaveController,
          resolve: {
            mlmodel: function () {
              return $scope.mlmodel;
            }
          }
        });

        mlmodelSave.result.then(function (entity) {
          $scope.mlmodel = entity;
          $scope.save(id);
        });
      };
    }]);

var MlmodelSaveController =
  function ($scope, $modalInstance, mlmodel) {
    $scope.mlmodel = mlmodel;

    

    $scope.ok = function () {
      $modalInstance.close($scope.mlmodel);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
