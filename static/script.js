var map = new google.maps.Map(document.getElementById('map'), {
    mapTypeId: google.maps.MapTypeId.ROADMAP
});
navigator.geolocation.getCurrentPosition(
    (position) => {
        const current_position = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
        };
        map.setCenter(current_position);
        map.setZoom(16)
    },
    () => {

    }
);
var infowindow = new google.maps.InfoWindow();

var marker, i;


google.maps.event.addListener(map, 'idle', function () {
    getListings(map.getBounds());
});


function getListings(bounds) {
    if (bounds == null) return
    restaurants = {
        's_lat': bounds.getSouthWest().lat(),
        's_lng': bounds.getSouthWest().lng(),
        'n_lat': bounds.getNorthEast().lat(),
        'n_lng': bounds.getNorthEast().lng()
    };
    $.ajax({
        type: "POST",
        dataType: 'json',
        url: "/resturants_in_map/",
        data: restaurants,
        success: function (restaurants_json) {
            restaurants = restaurants_json.restaurants
            for (i = 0; i < restaurants.length; i++) {
                marker = new google.maps.Marker({
                    position: new google.maps.LatLng(restaurants[i][1], restaurants[i][2]),
                    map: map
                });

                google.maps.event.addListener(marker, 'click', (function (marker, i) {
                    return function () {
                        infowindow.setContent(restaurants[i][0]);
                        infowindow.open(map, marker);
                    }
                })(marker, i));
            }
        }
    });
}