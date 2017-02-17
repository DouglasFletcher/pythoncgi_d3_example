


$("document").ready(function() {

	// click event
	$("#btnSubmit").click(function(){

		// get user input - notify user
		var result = $('input[type="radio"]:checked');
		if (result.length>0){
			if (result.val() == "1"){
				$('#divResult').html("getting exchange rate: Pound to Australia Dollar ...");
			} 
			else if (result.val() == "2"){
				$('#divResult').html("getting exchange rate: Pound to Euro ...");
			}
			else{
				$('#divResult').html("No currency selected");
			}
			// return data
			$.ajax({
				//url: "/exchangedashboard.com/cgi-bin/selectExchangeRates.py",
				url: "/cgi-bin/selectExchangeRates.py",
				type: "post",
				datatype: "html",
				data: {"result": result.val()},
				success: function(response){
					graphExchanges(response);
				}
			});
		}
	});
});

