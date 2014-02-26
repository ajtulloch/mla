// Declare app level module which depends on filters, and services
angular.module('app', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date', 'nvd3ChartDirectives'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/static/views/home/home.html', 
        controller: 'HomeController'})
      .otherwise({redirectTo: '/'});
  }]);
