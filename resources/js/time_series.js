// Controlling object.
// Pls follow call flow from html onto here.
// This creates a encapsulated namespace where we need not worry about JS 'this' playing wreck
// PS. JS Noob wrote this :-P

function TimeSeries(url_, id_, ctrl_id_) {
    var obj = {
        url : url_,
        id : id_,
        ctrl_id : ctrl_id_,
        init : function () {
            // co_ord of MG Road
            obj.map = L.map(obj.id).setView([12.97, 77.6], 12);
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png',{maxZoom : 18,}).addTo(obj.map);
        },
        draw : function () {
            $.getJSON(obj.url, obj.callback);
        },
        callback : function(locs) {
            obj.locs = locs;
            for (var i in obj.locs) {
                obj.locs[i]['datetime'] = new Date(obj.locs[i]['datetime']);
            }
            obj.addMarkers(locs);
            date_range = obj.get_date_range(obj.locs);
            ctrl = Controller(obj.ctrl_id, date_range[0], date_range[1]);
        },
        addMarkers : function(locs) {
            // plugin that helps de-clutter markers.
            // instead of adding marker to map. Add to the below. Then add the below to map
            var markers = L.markerClusterGroup();
            for (var i in locs) {
                var co_ord = locs[i]['co_ord'];
                var vol = locs[i]['volume'];
                // create marker with the proper icon
                var marker = LARGE_MARKERS.createMarker(locs[i]);

                // callback that shows volume of garbage
                marker.bindPopup('vol : ' + vol.toFixed(2) + '\nloc : ' + co_ord);
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
        get_date_range : function(locs) {
            var min = 0;
            var max = 0;
            for (var i = 0; i < locs.length; ++i) {
                var curr = locs[i]['datetime'];
                if (curr.getTime() < locs[min]['datetime'].getTime()) {
                    min = i;
                }
                if (curr.getTime() > locs[max]['datetime'].getTime()) {
                    max = i;
                }
            }

            return [new Date(locs[min]['datetime']), new Date(locs[max]['datetime'])];
        },
        clear : function() {
            obj.map.removeLayer(obj.markers);
        },
        redraw : function(from, to) {
            filtered_locs = [];
            for (var i in obj.locs) {
                var tmp = obj.locs[i]['datetime'];
                if (tmp.getTime() >= from.getTime() && tmp.getTime() <= to.getTime()) {
                    filtered_locs.push(obj.locs[i]);
                }
            }
            obj.clear();
            obj.addMarkers(filtered_locs);
        }
    };
    obj.init();
    return obj;
}

function Controller (id_, from_, to_) {
    var obj = {
        id : id_,
        init : function () {
            var parent = document.getElementById(obj.id);
            obj.slider = document.createElement('div');

            var bounds_min = new Date(from_);
            var bounds_max = new Date(to_);
            bounds_min = bounds_min.setDate(bounds_min.getDate() - 1);
            bounds_max = bounds_max.setDate(bounds_max.getDate() + 1);
            $(obj.slider).dateRangeSlider({
                bounds : {
                    min : bounds_min,
                    max : bounds_max,
                },
                defaultValues : {
                    min : from_,
                    max : to_,
                }
            });
            obj.btn = document.createElement('input');
            obj.btn.type = 'button';
            obj.btn.value = 'Refresh';
            obj.btn.onclick = obj.callback;

            parent.appendChild(obj.slider);
            parent.appendChild(document.createElement('BR'));
            parent.appendChild(obj.btn);
        },
        callback : function(ev) {
            var min_val = $(ctrl.slider).dateRangeSlider('min');
            var max_val = $(ctrl.slider).dateRangeSlider('max');
            time_series.redraw(min_val, max_val);
        },
    };
    obj.init();

    return obj;
}
