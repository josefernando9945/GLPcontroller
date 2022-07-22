//
// Charts
//

'use strict';

//
// Sales chart
//

var SalesChart = (function() {

	// Variables

	var $chart = $('#chart-sales');


	// Methods

	function init($this) {
		var salesChart = new Chart($this, {
			type: 'line',
			options: {
				scales: {
					yAxes: [{
						gridLines: {
							color: Charts.colors.gray[200],
							zeroLineColor: Charts.colors.gray[200]
						},
						ticks: {

						}
					}]
				}
			},
			data: {
				labels: ['test','Fev','Mar','Abr','Mai', 'Jun', 'Jul', 'Ago', 'paulo', 'Otu', 'Nov', 'Dez'],
				datasets: [{
					label: 'valor',
					data: [0, 20, 10, 30, 15, 40, 20, 60, 40, 40, 40, 60]
				}]
			}
		});

		// Save to jQuery object

		$this.data('chart', salesChart);

	};


	// Events

	if ($chart.length) {
		init($chart);
	}

});
