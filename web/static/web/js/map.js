function initMap(){
    var coord = {lat: -33.4488897,lng:-70.6692655};
    var map = new google.maps.Map(document.getElementById("mapa"),{
        zoom: 13,
        center: coord,
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}