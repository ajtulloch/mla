'use strict';

angular.module('app')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/tasks', {
        templateUrl: '/static/views/BatchTrainingRequest/Batchtrainingrequests.html',
        controller: 'BatchTrainingRequestController',
        resolve: {
          resolvedBatchTrainingRequest: ['BatchTrainingRequest', function (BatchTrainingRequest) {
            return BatchTrainingRequest.query();
          }]
        }
      })
    }]);
