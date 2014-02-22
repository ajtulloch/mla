(function() {
  'use strict';
  angular.module('frontendApp', []).config(function($routeProvider) {
    return $routeProvider.when('/', {
      templateUrl: 'views/main.html',
      controller: 'MainCtrl'
    }).otherwise({
      redirectTo: '/'
    });
  });

}).call(this);

/*
//@ sourceMappingURL=app.js.map
*/