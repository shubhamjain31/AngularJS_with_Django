var myApp = angular.module('app', []).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });

    myApp.controller("MainController", function ($scope, $http) {

        const data = JSON.parse(document.getElementById('all_employees').textContent);
        $scope.all_employees = data

        $scope.remove = function(id, index) {
            id_ = id['0'][0]
            var postReq = {
                method: 'DELETE',
                url: '/delete/employee/'+0,
                data: {id:id_},
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            
            $http(postReq).then(function (response) {
                if (response.data.deleted) {
                    $scope.Message = response.data.msg
                    $('#employee_msg').html(response.data.msg);
                    $scope.all_employees.splice(index,1);
                }
               
            }, function (error) {
            });
        }

});