// Controlling object.
// Pls follow call flow from html onto here.
// This creates a encapsulated namespace where we need not worry about JS 'this' playing wreck
// PS. JS Noob wrote this :-P

function Route(locations_, id_) {
    var obj = {
        locations : locations_,
        id : id_,
        init : function () {
            obj.map = L.map(obj.id).setView([12.97, 77.6], 11);
            obj.position = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png',{maxZoom : 18,});
            obj.position.addTo(obj.map);
            obj.co_ords = obj.get_co_ords(obj.locations);
        },
        draw : function() {
            MARKERS = MarkersFactory();
            obj.routing_options = obj.configRouteOptions()
            obj.route = L.Routing.control(obj.routing_options);
            obj.route.addTo(obj.map);
        },
        // Internal fns follows
        configRouteOptions : function () {
            obj.routing_lineOptions = {
                styles : [{
                    color : 'green',
                    opacity : 1,
                    weight : 2,
                },],
            };
            obj.routing_planOptions = {
                createMarker : function (i, wp, n) {
                    var vol = obj.locations[i]['cluster_center']['volume'];
                    var co_ord = obj.locations[i]['cluster_center']['co_ord'];
                    var marker;
                    if (i == 0) {
                        marker = L.marker(wp.latLng, {icon:MARKERS.largeGreenIcon,});
                    } else if (i == n-1) {
                        marker = L.marker(wp.latLng, {icon:MARKERS.largeRedIcon,});
                    } else {
                        marker = L.marker(wp.latLng, {icon:MARKERS.smallYellowIcon,});
                    }
                    marker.bindPopup('loc : ' + co_ord);

                    return marker;
                },
                addWaypoints : false,
                draggableWaypoints : false,
            };
            obj.routing_plan = L.Routing.plan(obj.co_ords, obj.routing_planOptions);
            obj.routing_options = {
                waypoints : obj.co_ords,
                collapsible : true,
                plan : obj.routing_plan,
                lineOptions : obj.routing_lineOptions,
                show : false,
            };
            return obj.routing_options;
        },
        get_co_ords : function (locs) {
            var co_ords = []
            for (i in locs) {
                co_ords.push(locs[i]['cluster_center']['co_ord']);
            }
            return co_ords;
        },
    };
    obj.init();

    return obj;
}
