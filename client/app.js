function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

function onClickedEstimatePrice(){
    console.log("Extimate Price button clicked!");
    var sqft = document.getElementById("uiSqft");
    var bathrooms=getBathValue();
    var bhk = getBHKValue();
    var location= document.getElementById("uiLocations");
    var extimatedPrice = document.getElementById("uiEstimatedPrice");

    console.log("Total sqft = "+sqft +" Bhk = " +bhk + " Bathrooms = "+bathrooms+" location = "+location );

//    var url = "http://127.0.0.1:5000/predict_home_price";
    var url = "/api/predict_home_price"
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        extimatedPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });

}

function onPageLoad(){
    console.log("page loaded")

//    var url = "http://127.0.0.1:5000/get_location_names";
    var url = "/api/get_location_names"

    $.get(url , function(data , status){
        console.log("Got responses from get_location_names request");
        var locations = data.locations;
        console.log(locations);
        var uiLocations = document.getElementById("uiLocations");
        $("#uiLocations").empty();
        for(var i in locations){
            var opt = new Option(locations[i]);
            $("#uiLocations").append(opt);
        }
    })
}

window.onload = onPageLoad
