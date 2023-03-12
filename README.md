if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(showPosition);
} else {
  console.log("Geolocation is not supported by this browser.");
}

function showPosition(position) {
  console.log("Latitude: " + position.coords.latitude +
  " Longitude: " + position.coords.longitude);
}
var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
    '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
    'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
}).addTo(mymap);

function showPosition(position) {
  var latlng = L.latLng(position.coords.latitude, position.coords.longitude);
  L.marker(latlng).addTo(mymap);
}

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(showPosition);
} else {
  console.log("Geolocation is not supported by this browser.");
}
var socket = io();

function showPosition(position) {
  var data = {
    latitude: position.coords.latitude,
    longitude: position.coords.longitude
  };
  socket.emit('location', data);
}

if (navigator.geolocation) {
  navigator.geolocation.watchPosition(showPosition);
} else {
  console.log("Geolocation is not supported by this browser.");
}
var socket = io();

function showPosition(position) {
  var data = {
    latitude: position.coords.latitude,
    longitude: position.coords.longitude
  };
  socket.emit('location', data);
}

if (navigator.geolocation) {
  navigator.geolocation.watchPosition(showPosition);
} else {
  console.log("Geolocation is not supported by this browser.");
}
