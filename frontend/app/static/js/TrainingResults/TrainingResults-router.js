'use strict';

angular.module('app')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/reports', {
        templateUrl: '/static/views/TrainingResults/Trainingresults.html',
        controller: 'TrainingResultsController',
        resolve:{
          resolvedTrainingResults: ['TrainingResults', function (TrainingResults) {
            return TrainingResults.query();
          }]
        }
      })
      .when('/reports/:reportId', {
        templateUrl: '/static/views/TrainingResults/analysis.html',
        controller: 'TrainingResultsCtrl'
      });
    }]);
