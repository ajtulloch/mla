'use strict';

angular.module('mlserver')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/trainingresults', {
        templateUrl: 'views/trainingresults/trainingresults.html',
        controller: 'TrainingresultsController',
        resolve:{
          resolvedTrainingresults: ['Trainingresults', function (Trainingresults) {
            return Trainingresults.query();
          }]
        }
      })
      .when('/trainingresults/:id', {
        templateUrl: 'views/trainingresults/trainingresults-detail.html',
        controller: 'TrainingresultsDetailController',
        resolve: {
          resolvedTrainingresult: ['Trainingresults, $route', function (Trainingresults, $route) {
            return Trainingresults.get({
              id: $route.current.params.id,
            });
          }]
        }
      })
    }]);
