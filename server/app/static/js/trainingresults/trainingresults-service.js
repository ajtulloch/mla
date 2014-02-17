'use strict';

angular.module('mlserver')
  .factory('Trainingresults', ['$resource', function ($resource) {
    return $resource('mlserver/trainingresults/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
