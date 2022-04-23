angular.module("MyApp", ['ngResource']);

angular.module('MyApp').controller("MyControler", function($scope, $resource, $timeout, $sce){
    var arrarypedal = [];

    $scope.refresh = function(){
        $resource('/pedal').get().$promise.then(function(result) {
            $scope.result = result;
            $scope.arrarypedal = arrarypedal;
        }).catch(function(error){
            //empty
        }).finally(function(){
            $timeout($scope.refresh, 5000);
        });
    };

    $scope.refresh();

});