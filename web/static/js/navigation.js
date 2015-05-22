
var app = angular.module('cau', []);

/* Controlarem les taules des d'aquí */
app.controller('NavController', function($scope, $http){
	$scope.showTickets = new Array();
	$scope.priorities = priorityArray;

	$scope.toggleTicket = function(getTicket){
		$scope.showTickets[getTicket] = $scope.showTickets[getTicket] === false ? true : false;
	};

	$scope.isToShow = function(getTicket){
		return $scope.showTickets[getTicket];
	}

	$scope.colourPriority = function(getPriority){
		return $scope.priorities[getPriority];
	}
});

var priorityArray = [
		"",						// Hi ha un espai per fer correspondre les claus de prioritats
		"panel-success", 		// baja
		"panel-info",			// media
		"panel-alert",			// alta
		"panel-warning",		// grave
		"panel-danger"			// critica
];