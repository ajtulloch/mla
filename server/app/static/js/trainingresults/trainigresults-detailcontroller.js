'use strict';

angular.module('mlserver')
  .controller('TrainingresultsDetailController', ['$scope', 'resolvedTrainingresult',
    function ($scope, resolvedTrainingresult) {
      $scope.trainingresult = resolvedTrainingresult;
    }]);
