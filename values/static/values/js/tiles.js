let watchID = navigator.geolocation.watchPosition(position => {
    // console.log(position.coords.latitude, position.coords.longitude)
    document.querySelector('#lat').innerHTML = 'lat: ' + position.coords.latitude
    document.querySelector('#lon').innerHTML = 'lon: ' + position.coords.longitude
})