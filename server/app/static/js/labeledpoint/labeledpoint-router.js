'use strict';

angular.module('mlserver')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/labeledpoints', {
        templateUrl: 'views/labeledpoint/labeledpoints.html',
        controller: 'LabeledpointController',
        resolve:{
          resolvedLabeledpoint: ['Labeledpoint', function (Labeledpoint) {
            return Labeledpoint.query();
          }]
        }
      })
    }]);
