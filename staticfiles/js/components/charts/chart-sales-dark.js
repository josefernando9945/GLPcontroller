//
// Charts
//

'use strict';

//
// Sales chart
//


	$.ajax({
		url: 'api/relatorio_anual',
		success: function (response){

			var ctx = document.getElementById('chartSalesDark').getContext('2d');
             var chartSales = new Chart(ctx, {
                     type: 'line',
                     options: {
                         scales: {
                             yAxes: [{
                                 gridLines: {
                                     color: Charts.colors.gray[700],
                                     zeroLineColor: Charts.colors.gray[700]
                                 },
                                 ticks: {}
                             }]
                         }
                     },
                     data: {
                         labels: response.labels,
                         datasets: [{
                             label: 'valor',
                             data: response.data

                         }]
                     }


             })

             var chartSalesDark = new chart(ctx, chartSales)

                 $this.data('chart', chartSalesDark);
		}
	});
