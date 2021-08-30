var myApp = angular.module('app', []).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });

    myApp.controller("MainController", function ($scope, $http) {

        const data = JSON.parse(document.getElementById('all_employees').textContent);
        $scope.all_employees = data

});