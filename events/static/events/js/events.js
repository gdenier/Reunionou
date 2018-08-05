document.addEventListener("DOMContentLoaded", function () {
  var sections = document.getElementsByTagName("section")
  if (sections.length > 0) {
    for (let i = 0; i < sections.length; i++) {      
      if (sections[i].id == 'new-event') {
        var map = L.map('new-event-map', {
          center: [48.856614, 2.3522219000000177], 
          zoom: 13
        })
        
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZWRlbW90cyIsImEiOiJjamtncmc5ejgwbW1vM2tzNmhhcTA4b3RxIn0.TQhmm2_0ywVp2MrNLRUm3Q', {
          maxZoom: 18,
          attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
          '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ',
          id: 'mapbox.streets',
        }).addTo(map);

        var observer = new MutationObserver(function (events) {
          for (var event of events) {
            if (event.type == "attributes") {
              if (event.target.classList.contains("is-active")) {
                map.invalidateSize(true)
              }
            }
          }
        })

        observer.observe(map.getContainer().closest(".step-content"), {
          attributes: true,
          attributeFilter: ['class'],
          childList: false,
          characterData: false
        })
      }
    }
  }
})