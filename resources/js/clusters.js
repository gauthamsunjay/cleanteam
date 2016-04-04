// Controlling object.
// Pls follow call flow from html onto here.
// This creates a encapsulated namespace where we need not worry about JS "this" playing wreck
// PS. JS Noob wrote this :-P

function clusters(url_, id_) {
    var obj = {
        url : url_,
        id : id_,
        init : function () {
            // co_ord of MG Road
            obj.map = L.map(obj.id).setView([12.97, 77.6], 11);
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
            var markers = L.markerClusterGroup();
            obj.components_markers = {};
            for (var i in data) {
                // create large cluster marker
                var cluster_co_ord = data[i]['cluster_center'];
                var cluster_marker = L.marker(cluster_co_ord, {icon : Markers.largeRedIcon}).addTo(obj.map);
                var cluster_id = cluster_marker['_leaflet_id'];

                // store markers of components for each cluster in dict.
                // so we can use this to add and remove components markers when needed...
                obj.components_markers[cluster_id] = [];

                for (var j in data[i]['components']) {
                    console.log(cluster_marker._leaflet_id);
                    var co_ord = data[i]['components'][j];
                    var marker = L.marker(co_ord, {icon : Markers.smallRedIcon});
                    obj.components_markers[cluster_id].push(marker);
                }

                // register callback for big cluster icon.
                cluster_marker.on('mouseover', function (e) {
                    var cluster_id = e['target']['_leaflet_id'];
                    for (var i in obj.components_markers[cluster_id]) {
                        obj.map.addLayer(obj.components_markers[cluster_id][i]);
                    }
                });
                cluster_marker.on('mouseout', function (e) {
                    var cluster_id = e['target']['_leaflet_id'];
                    for (var i in obj.components_markers[cluster_id]) {
                        obj.map.removeLayer(obj.components_markers[cluster_id][i]);
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
