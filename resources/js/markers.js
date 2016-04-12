function MarkersFactory(up_, down_, size_) {
    var markers = {
        up : up_,
        down : down_,
        size : size_ ? size_ : 'large',
        largeRedIcon : L.icon({
            iconUrl : 'imgs/red_marker.png',
            iconSize : [30,50],
        }),
        largeYellowIcon : L.icon({
            iconUrl : 'imgs/yellow_marker.png',
            iconSize : [30,50],
        }),
        largeGreenIcon : L.icon({
            iconUrl : 'imgs/green_marker.png',
            iconSize : [30,50],
        }),
        smallRedIcon : L.icon({
            iconUrl : 'imgs/red_marker.png',
            iconSize : [15,25],
        }),
        smallYellowIcon : L.icon({
            iconUrl : 'imgs/yellow_marker.png',
            iconSize : [15,25],
        }),
        smallGreenIcon : L.icon({
            iconUrl : 'imgs/green_marker.png',
            iconSize : [15,25],
        }),
        createMarker : function (location) {
            var co_ord = location['co_ord'];
            var volume = location['volume'];
            var icon_ = markers.getIconByVolume(volume);
            var marker = L.marker(co_ord, {icon : icon_});

            return marker;
        },
        getIconByVolume : function(vol) {
            var icon = markers.largeRedIcon;
            if (markers.size == 'small') {
                icon = markers.smallRedIcon;
                if (vol < markers.up) {
                    icon = markers.smallYellowIcon;
                }
                if (vol < markers.down) {
                    icon = markers.smallGreenIcon;
                }
            } else if (markers.size == 'large') {
                icon = markers.largeRedIcon;
                if (vol < markers.up) {
                    icon = markers.largeYellowIcon;
                }
                if (vol < markers.down) {
                    icon = markers.largeGreenIcon;
                }
            } else {
                icon = markers.largeRedIcon;
            }
            return icon;
        }
    };
    return markers;
}
