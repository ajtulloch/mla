'use strict';

angular.module('mlserver')
  .controller('LabeledpointController', ['$scope', '$modal', 'resolvedLabeledpoint', 'Labeledpoint',
    function ($scope, $modal, resolvedLabeledpoint, Labeledpoint) {

      $scope.labeledpoints = resolvedLabeledpoint;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.labeledpoint = Labeledpoint.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Labeledpoint.delete({id: id},
          function () {
            $scope.labeledpoints = Labeledpoint.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Labeledpoint.update({id: id}, $scope.labeledpoint,
            function () {
              $scope.labeledpoints = Labeledpoint.query();
              $scope.clear();
            });
        } else {
          Labeledpoint.save($scope.labeledpoint,
            function () {
              $scope.labeledpoints = Labeledpoint.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.labeledpoint = {
          
          "label": "",
          
          "features": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var labeledpointSave = $modal.open({
          templateUrl: 'labeledpoint-save.html',
          controller: LabeledpointSaveController,
          resolve: {
            labeledpoint: function () {
              return $scope.labeledpoint;
            }
          }
        });

        labeledpointSave.result.then(function (entity) {
          $scope.labeledpoint = entity;
          $scope.save(id);
        });
      };
    }]);

var LabeledpointSaveController =
  function ($scope, $modalInstance, labeledpoint) {
    $scope.labeledpoint = labeledpoint;

    

    $scope.ok = function () {
      $modalInstance.close($scope.labeledpoint);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
