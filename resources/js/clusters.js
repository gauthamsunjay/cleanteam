// Controlling object.
// Pls follow call flow from html onto here.
// This creates a encapsulated namespace where we need not worry about JS "this" playing wreck
// PS. JS Noob wrote this :-P

function Clusters(url_, id_) {
    var obj = {
        url : url_,
        id : id_,
        init : function () {
            // co_ord of MG Road, Bangalore-001
            obj.map = L.map(obj.id).setView([12.97, 77.6], 11);
            L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png",{maxZoom : 18,}).addTo(obj.map);
        },
        draw : function () {
            $.getJSON(obj.url, obj.callback);
        },
        callback : function(clusters) {
            obj.clusters = clusters;
            obj.addMarkers(clusters);
        },
        addMarkers : function(clusters) {
            obj.components_markers = {};
            for (var i in clusters) {
                // create large cluster marker
                var cluster_co_ord = clusters[i]['cluster_center'];
                var cluster_marker = LARGE_MARKERS.createMarker({
                    'co_ord' : cluster_co_ord,
                    'volume' : clusters[i]['volume'],
                });
                cluster_marker.addTo(obj.map);

                var cluster_id = cluster_marker['_leaflet_id'];

                // store markers of components for each cluster in dict.
                // so we can use this to add and remove components markers when needed...
                obj.components_markers[cluster_id] = [];

                var markers = L.markerClusterGroup();
                for (var j in clusters[i]['components']) {
                    var marker = SMALL_MARKERS.createMarker(clusters[i]['components'][j]);
                    markers.addLayer(marker);
                }
                obj.components_markers[cluster_id] = markers;

                // register callback for big cluster icon.
                var vol = clusters[i]['volume'];
                cluster_marker.bindPopup("vol : " + vol.toFixed(2));
                cluster_marker.on('click', function (e) {
                    var cluster_id = e['target']['_leaflet_id'];
                    var isdrawn = obj.map.hasLayer(obj.components_markers[cluster_id]);
                    if (!isdrawn) {
                        this.openPopup();
                        obj.map.addLayer(obj.components_markers[cluster_id]);
                    } else {
                        this.closePopup();
                        obj.map.removeLayer(obj.components_markers[cluster_id]);
                    }
                });
            }
        },
        clear : function() {
            obj.map.removeLayer(obj.markers);
        },
    };
    obj.init();
    return obj;
}
