'use strict';

angular.module('app')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/Trainingresults', {
        templateUrl: 'views/TrainingResults/Trainingresults.html',
        controller: 'TrainingResultsController',
        resolve:{
          resolvedTrainingResults: ['TrainingResults', function (TrainingResults) {
            return TrainingResults.query();
          }]
        }
      })
    }]);
