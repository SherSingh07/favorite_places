/*
------------------------------------------------------------------------------
				PLACES MANAGER ANGULAR JS SCRIPT
------------------------------------------------------------------------------
*/

// creating the module
var myApp = 
angular
.module("placeModule", [])
.controller("placeController", function($scope) {	

	$scope.message = "Places Manager Demo By Singh";

	// some place objects
	$scope.places = [ ];


	// function to add new place
	$scope.addTask = function() {
		//$scope.places.push({ title: $scope.new_place, completed: false});
	}
});

myApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
