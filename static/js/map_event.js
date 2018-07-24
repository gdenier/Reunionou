var lat = 10;
var lng = 10;

var mymap = L.map('mapid')
var layer = new L.LayerGroup();
mymap.addLayer(layer);

function getSetAddress(mymap, layer)
{
    corner_1 = mymap.getBounds().getNorthWest();
    corner_2 = mymap.getBounds().getSouthEast();

    $.ajax({
        url:'/events/ajax/getsetevent/',
        data: {
            'lat_inf': corner_1['lat'],
            'lng_inf': corner_1['lng'],
            'lat_sup': corner_2['lat'],
            'lng_sup': corner_2['lng']
        },
        datatype: 'json',
        type: 'GET',
        success: function(data){
            var data = $.parseJSON(data)
            
            layer.clearLayers();

            for(var k in data){
                var marker = L.marker([data[k]['lat'], data[k]['lng']]).addTo(layer);
                marker.bindPopup("<center><b>"+data[k]['title']+"</b></center><br>"+data[k]['address']);
            }
        }
    });
}

function getPos(position)
{
    lat = position.coords.latitude;
    lng = position.coords.longitude;

    var coord = new L.LatLng(lat, lng);

    mymap.setView(coord, 10);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ',
        id: 'mapbox.streets'
    }).addTo(mymap);

    getSetAddress(mymap, layer);

}

mymap.on('zoomend', function(){
    getSetAddress(mymap, layer);
});

mymap.on('moveend', function(){
    getSetAddress(mymap, layer);
});

if(navigator.geolocation)
{
    navigator.geolocation.getCurrentPosition(getPos);
}


