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
    }]);
