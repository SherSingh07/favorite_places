/*
------------------------------------------------------------------------------
				PLACES MANAGER ANGULAR JS SCRIPT
------------------------------------------------------------------------------
*/

// creating the module
var myApp = 
angular
.module("placeModule", [])
.controller("placeController", function($scope, $http) {	

	$scope.message = "Places Manager Demo By Singh";

	// some place objects
	$scope.places = [ ];
	$scope.categories = [{title: 'aaa'}];

        $scope.GetAllCategories = function () {
             $http.get("http://localhost:8000/categories/")
                 .then(function(response){ 
                     $scope.categories = response.data; 
                 });
        };
            
	// function to add new place
	$scope.addTask = function() {
		//$scope.places.push({ title: $scope.new_place, completed: false});
	}

        // show categories on start
        $scope.GetAllCategories();
});

myApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
