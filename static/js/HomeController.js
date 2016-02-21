angular.module('app').controller('HomeController', ['$scope', '$http', function($scope, $http){
	console.log("controller works");
	$http({
	  method: 'GET',
	  url: '/get_target_data'
	}).then(function successCallback(response) {
	     console.log(response)
	  }, function errorCallback(response) {
	     console.log(response);
	  });

	
        $http.post('/profile', {'key':"5005"})
             .success(function(){alert('ok')})
             .error(function(){alert('fail')});
    

}]);