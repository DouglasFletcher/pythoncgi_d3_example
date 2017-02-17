


$("document").ready(function() {

	window.graphExchanges = function (inputVal){

		// canvas dimensions
		var margin = {top: 30, right: 20, bottom: 30, left: 50},
			width = 600 - margin.left - margin.right,
			height = 270 - margin.top - margin.bottom;

		// parse date time
		var parseDate = d3.time.format("%Y-%m-%d").parse;

		// set ranges
		var x = d3.time.scale().range([0, width]);
		var y = d3.scale.linear().range([height, 0]);

		// Define the axis
		var xAxis = d3.svg.axis().scale(x)
			.orient("bottom").ticks(15);

		var yAxis = d3.svg.axis().scale(y)
			.orient("left").ticks(15);

		// Define line
		var valueline = d3.svg.line()
			.x(function(d) {return x(d.period)})
			.y(function(d) {return y(d.values)});

		// Add svg canvas
		$("#divResult").html("");
		var svg = d3.select("#divResult")
			.append("svg")
				.attr("width", width + margin.left + margin.right)
				.attr("height", height + margin.top + margin.bottom)
			.append("g")
				.attr("transform",
					"translate(" + margin.left + "," + margin.top + ")");

		// get the data
		data = jQuery.parseJSON(inputVal);

		// parse values
		$.each(data, function(index, value){
			value.period = parseDate(value.period);
			value.values = value.values;
		})

		// scale the range
		x.domain(d3.extent(data, function(d) { return d.period;}));
		y.domain([0, d3.max(data, function(d) {return d.values;})]);

		// Add valueline
		svg.append("path")
			.attr("class", "line")
			.attr("d", valueline(data));

		// Add the X Axis
		svg.append("g")
			.attr("class", "x axis")
			.attr("transform", "translate(0," + height + ")")
			.call(xAxis);

		// Add the Y axis
		svg.append("g")
			.attr("class", "y axis")
			.call(yAxis);

	}
});














