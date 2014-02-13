'use strict';

angular.module('mlserver')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/mlmodels', {
        templateUrl: 'views/mlmodel/mlmodels.html',
        controller: 'MlmodelController',
        resolve:{
          resolvedMlmodel: ['Mlmodel', function (Mlmodel) {
            return Mlmodel.query();
          }]
        }
      })
    }]);
