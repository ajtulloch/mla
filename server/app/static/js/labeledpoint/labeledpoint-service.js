'use strict';

angular.module('mlserver')
  .factory('Labeledpoint', ['$resource', function ($resource) {
    return $resource('mlserver/labeledpoints/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
