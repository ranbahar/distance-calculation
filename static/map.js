var map;
var circle;
var marker;

function initialize() {
    var mapOptions = {
        center: { lat: 32.07519345111358, lng: 34.77496212125395 },
        zoom: 12
    };

    map = new google.maps.Map(document.getElementById('map'), mapOptions);

    // Set marker on default position
    var defaultPosition = new google.maps.LatLng(32.07519345111358, 34.77496212125395);
    setMarker(defaultPosition);


    // Draw a circle on default position
    placeCircle(defaultPosition);

    map.addListener('click', function(event) {
        placeCircle(event.latLng);
        setMarker(event.latLng);
    });

        map.addListener('contextmenu', function(event) {
        showLatLng(event.latLng);
    });
}

function showLatLng(latLng) {
    var lat = latLng.lat();
    var lng = latLng.lng();
    alert("Latitude: " + lat + "\nLongitude: " + lng);
}

function placeCircle(location) {
    if (circle) {
        circle.setMap(null);
    }

    var circleOptions = {
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#FF0000',
        fillOpacity: 0.35,
        map: map,
        center: location,
        radius: 1000
    };

    circle = new google.maps.Circle(circleOptions);
}

function setMarker(location) {
    if (marker) {
        marker.setMap(null);
    }

    marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

google.maps.event.addDomListener(window, 'load', initialize);
