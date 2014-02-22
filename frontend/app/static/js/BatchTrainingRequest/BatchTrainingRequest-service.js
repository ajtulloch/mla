'use strict';

angular.module('app')
  .factory('BatchTrainingRequest', ['$resource', function ($resource) {
    return $resource('app/Batchtrainingrequests/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
