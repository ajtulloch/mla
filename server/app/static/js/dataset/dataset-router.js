'use strict';

angular.module('mlserver')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/datasets', {
        templateUrl: 'views/dataset/datasets.html',
        controller: 'DatasetController',
        resolve:{
          resolvedDataset: ['Dataset', function (Dataset) {
            return Dataset.query();
          }]
        }
      })
    }]);
