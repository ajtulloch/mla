app.controller(
  'TrainingResultsCtrl',
  ['$scope', '$routeParams', 'TrainingResults',
   function($scope, $routeParams, TrainingResults) {
     var result = TrainingResults.get({id:$routeParams.id});
     $scope.id = result.id
     $scope.jsonResport = angular.fromJSON(result.jsonString)
   }
  ]
)

