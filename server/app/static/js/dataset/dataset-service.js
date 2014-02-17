'use strict';

angular.module('mlserver')
  .factory('Dataset', ['$resource', function ($resource) {
    return $resource('mlserver/datasets/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
