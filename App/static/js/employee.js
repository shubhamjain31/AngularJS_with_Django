var myApp = angular.module('app', [], function($httpProvider){
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });

    myApp.controller("MainController", function ($scope, $http) {

        // get data from object type variable from html
        const data = JSON.parse(document.getElementById('obj').textContent);
        $scope.employee = data[0]


        $scope.submit = function() {
            if(!data){

                var postReq = {
                    method: 'POST',
                    url: '/add/employee/',
                    data: $scope.employee,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                };
            }
            else{
                id_ = $scope.employee.id
                var postReq = {
                    method: 'PUT',
                    url: '/edit/employee/'+id_,
                    data: $scope.employee,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                };
            }

            $http(postReq).then(function (response) {
                $scope.employee = {}
                if (response.data.error) {
                    $scope.Message = response.data.msg
                    $('#employee_msg').html(response.data.msg);
                }
                else{
                    $scope.Message = response.data.msg
                    $('#employee_msg').html(response.data.msg);
                }
               
            }, function (error) {
            });
        }

});