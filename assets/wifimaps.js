$(document).ready(function() {
    var map = new L.Map('map', {
        center: new L.LatLng(47.5670, -122.3000),
        zoom: 13
    });
    L.tileLayer(
        'http://{s}.tile.cloudmade.com/67dabcd23bb142c79b873e9dd0cf6b89/997/256/{z}/{x}/{y}.png',
        {
            attribution: 'Wifi Data provided by andrewx. Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery &copy; <a href="http://cloudmade.com">CloudMade</a>',
            maxZoom: 20
        }
    ).addTo(map);


    var controls = L.control.layers(null, map, {collapsed: false});
     
    controls.addTo(map);
    $.get("/littledata.geo.json").success(function(data) {
       L.geoJson(data['features']).addTo(map);
    });
});
