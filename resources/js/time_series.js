// Controlling object.
// Pls follow call flow from html onto here.
// This creates a encapsulated namespace where we need not worry about JS "this" playing wreck
// PS. JS Noob wrote this :-P

function time_series(url_, id_) {
    var obj = {
        url : url_,
        id : id_,
        init : function () {
            // co_ord of MG Road
            obj.map = L.map(obj.id).setView([12.97, 77.6], 12);
            L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png",{maxZoom : 18,}).addTo(obj.map);
        },
        draw : function () {
            $.getJSON(obj.url, obj.callback);
        },
        callback : function(data) {
            obj.data = data;
            obj.addMarkers(data);
        },
        addMarkers : function(data) {
            // plugin that helps de-clutter markers.
            // instead of adding marker to map. Add to the below. Then add the below to map
            var markers = L.markerClusterGroup();
            for (var i in data) {
                var co_ord = data[i]['co_ord'];
                var vol = data[i]['volume'];
                // select marker based on volume
                var icon_ = Markers.largeRedIcon;
                if (vol < 50) {
                    icon_ = Markers.largeYellowIcon;
                }
                if (vol < 20) {
                    icon_ = Markers.largeGreenIcon;
                }
                // create marker with the proper icon
                var marker = L.marker(co_ord, {icon : icon_});

                // callback that shows volume of garbage
                marker.bindPopup("" + vol.toFixed(2));
                marker.on('mouseover', function (e) {
                    this.openPopup();
                });
                marker.on('mouseout', function (e) {
                    this.closePopup();
                });

                // add to markerClusterGroup
                markers.addLayer(marker);
            }

            obj.markers = markers;
            // add to map
            obj.map.addLayer(markers);
        },
        clear : function() {
            obj.map.removeLayer(obj.markers);
        },
    };
    obj.init();
    return obj;
}
