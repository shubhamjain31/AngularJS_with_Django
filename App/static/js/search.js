alert('sk')
var myApp = angular.module('app', [], function($httpProvider){
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
      console.log('kdkdkfkdddd')
    }).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });

    myApp.controller("MainController", function ($scope, $http) {
         console.log('kdkdkfkdddd')

        // const data = JSON.parse(document.getElementById('all_employees').textContent);
        // $scope.all_employees = data

        $scope.search_exmployee = function() {
            console.log('kdkdkfk')
            var postReq = {
                method: 'POST',
                url: '/search/',
                data: {},
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            
            $http(postReq).then(function (response) {
                // if (response.data.deleted) {
                //     $scope.Message = response.data.msg
                //     $('#employee_msg').html(response.data.msg);
                //     $scope.all_employees.splice(index,1);
                // }
               
            }, function (error) {
            });
        }

});