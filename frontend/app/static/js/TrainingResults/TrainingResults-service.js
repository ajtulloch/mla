'use strict';

angular.module('app')
  .factory('TrainingResults', ['$resource', function ($resource) {
    return $resource('app/Trainingresults/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
