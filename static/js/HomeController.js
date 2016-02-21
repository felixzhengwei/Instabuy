angular.module('app').controller('HomeController', ['$scope', '$http', function($scope, $http){
	console.log("controller works");
	$scope.productInfo = {};
	$http({
	  method: 'GET',
	  url: '/get_target_data'
	}).then(function successCallback(response) {
	     console.log(response)
	     $scope.productInfo['title'] = response.data.product_composite_response.items[0].general_description;
	     $scope.productInfo['price'] = response.data.product_composite_response.items[0].online_price.list_price;
	     $scope.productInfo['image'] = response.data.product_composite_response.items[0].image.external_primary_image_url[0];
	     jQuery("#image").attr('src',$scope.productInfo.image);
	  }, function errorCallback(response) {
	     console.log(response);
	  });

	$http({
	  method: 'GET',
	  url: '/get_product_list'
	}).then(function successCallback(response) {
	     console.log(response)
	  }, function errorCallback(response) {
	     console.log(response);
	  });


	$scope.checkKey = function(event){
		if(event.keyCode === 13){
			$scope.send();
		}
	}

	$scope.send = function(){
		var value = $("#put").val();
		 $http.post('/profile', {'key':value})
             .success(function(){alert('ok')})
             .error(function(){alert('fail')});
	}
	
       

   

    $http({
	  method: 'GET',
	  url: '/get_target_data'
	}).then(function successCallback(response) {
	     console.log(response)
	  }, function errorCallback(response) {
	     console.log(response);
	  });

}]);