// Controlling object.
// Pls follow call flow from html onto here.
// This creates a encapsulated namespace where we need not worry about JS "this" playing wreck
// PS. JS Noob wrote this :-P

function TimeSeries(url_, id_, ctrl_id_) {
    var obj = {
        url : url_,
        id : id_,
        ctrl_id : ctrl_id_,
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
            for (var i in obj.data) {
                obj.data[i]['datetime'] = new Date(obj.data[i]['datetime']);
            }
            obj.addMarkers(data);
            date_range = obj.get_date_range(obj.data);
            ctrl = Controller(obj.ctrl_id, date_range[0], date_range[1]);
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
        get_date_range : function(data) {
            var min = 0;
            var max = 0;
            for (var i = 0; i < data.length; ++i) {
                var curr = data[i]['datetime'];
                if (curr.getTime() < data[min]['datetime'].getTime()) {
                    min = i;
                }
                if (curr.getTime() > data[max]['datetime'].getTime()) {
                    max = i;
                }
            }

            return [new Date(data[min]['datetime']), new Date(data[max]['datetime'])];
        },
        clear : function() {
            obj.map.removeLayer(obj.markers);
        },
        redraw : function(from, to) {
            filtered_data = [];
            for (var i in obj.data) {
                var tmp = obj.data[i]['datetime'];
                if (tmp.getTime() >= from.getTime() && tmp.getTime() <= to.getTime()) {
                    filtered_data.push(obj.data[i]);
                }
            }
            obj.clear();
            obj.addMarkers(filtered_data);
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
            obj.slider = document.createElement("div");

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
            obj.btn = document.createElement("input");
            obj.btn.type = "button";
            obj.btn.value = "Refresh";
            obj.btn.onclick = obj.callback;

            parent.appendChild(obj.slider);
            parent.appendChild(document.createElement("BR"));
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
