

function getLocation() {
    console.log("1");
    if(navigator.geolocation) {
        console.log("2");
        locationObtained({
            coords: {
                latitude: 32.489472,
                longitude: -117.03091199999999
            }
        });

        navigator.geolocation.getCurrentPosition(locationObtained);
    }
    else {
        console.error("Browser does not support Geolocation");
    }
}

function locationObtained(position) {
    console.log("3");
    console.log("Current location", position);

    let data = {
        lat: position.coords.latitude,
        lon: position.coords.longitude
    };

    $.ajax({
        url: "/api/weather",
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(res){
            console.log("Server says: ", res);

            // display the weather informatio on html
            //res.current.weather[0].icon
        },
        error: function(details) {
            console.error("Error sending data", details);
        }
    });
}

function init() {
    console.log("Flask page");

    getLocation();
}


window.onload = init;