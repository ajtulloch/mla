'use strict';

angular.module('mlserver')
  .factory('Mlmodel', ['$resource', function ($resource) {
    return $resource('mlserver/mlmodels/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
