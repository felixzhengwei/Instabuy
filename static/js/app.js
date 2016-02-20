'use strict';   

var app = angular.module('app', [
 'ngRoute', 'ngResource'
]);

app.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '../static/partials/home.html',
                 controller: 'HomeController'
             }).
             when('/login', {
                 templateUrl: '../static/partials/login.html',
                 controller: 'LoginController'
             }).
             when('/signup', {
                 templateUrl: '../static/partials/signup.html',
                 controller: 'SignupController'
             }).
             otherwise({
                 redirectTo: '/'
             });
}]);