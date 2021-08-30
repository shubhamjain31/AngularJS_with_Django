var myApp = angular.module('app', [], function($httpProvider){
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    });

    myApp.controller("MainController", function ($scope, $http) {

        $scope.submit = function() {
            var postReq = {
                method: 'POST',
                url: '/add/employee/',
                data: $scope.employee,
                headers: {
                    'Content-Type': 'application/json'
                }
            };

            $http(postReq).then(function (response) {
                $scope.employee = {}
                if (response.data.error) {
                    $scope.Message = response.data.msg
                    $('#employee_error_msg').html(response.data.msg);
                }
                else{
                    $scope.Message = response.data.msg
                    $('#employee_save_msg').html(response.data.msg);
                }
               
            }, function (error) {
            });
        }

});