angular.module('app').controller('HomeController', ['$scope', '$http', function($scope, $http){
	console.log("controller works");
	var array = [ 'PS4 Console',
				'Nikon D3300 DX-format DSLR Bundle',
				'Pebble Time Steel Smartwatch',
				'GoPro Camera HERO',
			   	'Bose SoundLink Speaker',
			   	'TomTom Via GPS',
			   	'Panasonic Sensor Microwave',
			   	'LG 55 1080p HD TV',
			   	'Microsoft Surface Pro 4',
			   	'WD External Hard Drive',
				'Beats Solo 2 Wireless Headphones']
	$scope.products = {
		'PS4 Console':'50522463',
				'Nikon D3300 DX-format DSLR Bundle':'21490248', 
				 'Pebble Time Steel Smartwatch':'49124627',
				 'GoPro Camera HERO':'18760721',
			    'Bose SoundLink Speaker':'18854140',
			    'TomTom Via GPS':'21456407',
			   	'Panasonic Sensor Microwave':'16510846',
			   'LG 55 1080p HD TV':'17221644', 
			   	'Microsoft Surface Pro 4':'50308839', 
			   'WD External Hard Drive':'14881813', 
				 'Beats Solo 2 Wireless Headphones':'16696652'
	}			
	$scope.productInfo = {};
	$scope.price_list = [];

	$( "#put" ).autocomplete({
			      source: array
			    });

	$scope.getRandomInt = function(min, max) {
  		return Math.floor(Math.random() * (max - min)) + min;
	}

	$scope.getResult = function(){
		$http({
		  method: 'GET',
		  url: '/get_target_data'
		}).then(function successCallback(response) {
		     console.log(response)
		     $scope.productInfo['title'] = response.data.product_composite_response.items[0].general_description;
		     $scope.productInfo['price'] = response.data.product_composite_response.items[0].online_price.list_price;
		     $scope.productInfo['image'] = response.data.product_composite_response.items[0].image.external_primary_image_url[0];
		     $scope.productInfo['price_list'] = response.data.price_list
		     $scope.productInfo['balance'] = response.data.balance
		     jQuery("#image").attr('src',$scope.productInfo.image);
		     $(".jumbotron").css({'display':"block"});

		     for(var i = 0; i< 11; i++){
		     	$scope.price_list.push(parseFloat($scope.productInfo['price'])*Math.floor((Math.random() * 1.2) + 0.6));
		     }
		  }, function errorCallback(response) {
		     console.log(response);
		  });
	}
	


	$scope.checkKey = function(event){
		if(event.keyCode === 13){
			$scope.send();
		}
	}

	$scope.send = function(){
		var value = $("#put").val();
		var request = $scope.products[value];
		 $http.post('/profile', {'key':request})
             .success(function(){$scope.getResult();})
             .error(function(){}); 
	}

	$scope.buy = function(){
		var request = Math.floor($scope.productInfo['price']);
		 $http.post('/buy', {'key':request})
             .success(function(){
             	$http({
				  method: 'GET',
				  url: '/get_response'
				}).then(function successCallback(response) {
				     if(response.data === "True") {
				     	// $scope.productInfo['balance'] = response.data.newBalance
				     	$(".message").css({"display":"block"});
				     	$scope.getResult();
				     } else {
				     	$('#head').text("Transaction failed");
				     	$(".message").css({"display":"block"});
				     }
				  }, function errorCallback(response) {
				   	 console.log("nah");
				  });
             })
             .error(function(){}); 
	}

	$scope.chart = function () {
			$(".chart").css({'display':"block"});
    		var dataArray = [];
    		var value = $scope.productInfo['price'];
		    $('#container').highcharts({
		        title: {
		            text: 'Current Price for',
		            x: -20 //center
		        },
		        subtitle: {
		            text: 'Source: Target',
		            x: -20
		        },
		        xAxis:{
		        	type: "datetime"
		        },
		        yAxis: {
		            title: {
		                text: 'Price ($)'
		            },
		            plotLines: [{
			        	color: '#ff0000',
			        	width: 2,
			        	value: 250
		        	}]
		        },
		        tooltip: {
		            valueSuffix: ' $'
		        },
		        legend: {
		            layout: 'vertical',
		            align: 'right',
		            verticalAlign: 'middle',
		            borderWidth: 0
		        },
		        series: [{
		            name: "Price",
		            data: []
		        }],
		       
		    });
		    function populateData(){
		    	for (var i = 0; i < 10; i++){
		    		dataArray.push([Date.UTC(2016, 2, 12+i), $scope.productInfo.price_list[i]]);       
		    	}
             };	
		    populateData();
		    		var time = 3000;
		        	var chart = $('#container').highcharts();
		        	var scenario = 0;
		        	var firstValue = dataArray[0];
		        	dataArray.forEach(function(data) {
        				setTimeout(function(){
        					chart.series[0].addPoint(data);
        					if(data[1] < value){
        						var name = $scope.productInfo['title'];
								var money = $scope.productInfo['price'];
								 $http.post('/message', {'name':name,
											"price":money})
						             .success(function(){})
						             .error(function(){}); 
								value = value + 100000;
        						// while(!keepGoing){
        						// 	//do nothing
        						// }
        						
        					}
        				},time);
        				time+=6000;
        			}); 
        		}
        	
}]);