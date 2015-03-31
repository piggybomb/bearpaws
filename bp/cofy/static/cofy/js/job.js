var chartTitle;
var selectedData;
//var jobData;

function generateChart(){
	var ctx = document.getElementById("canvas").getContext("2d");
	if (typeof window.myLine != 'undefined'){
		window.myLine.destroy();
	};
	chartTitle = $(".form-control").val();
	selectedData = jobData[chartTitle];
	var lineChartData = {
		labels: ["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022"],
		datasets: [
			{
				label: chartTitle,
	            fillColor : "rgba(180,0,0,0.2)",
	            strokeColor : "rgba(180,0,0,1)",
	            pointColor : "rgba(180,0,0,1)",
	            pointStrokeColor : "#fff",
	            pointHighlightFill : "#fff",
	            pointHighlightStroke : "rgba(180,0,0,1)",
	            data: selectedData
			}
		]
	};
	window.myLine =  new Chart(ctx).Line(lineChartData, {
		responsive: true
	});
	console.log("hi")
};




