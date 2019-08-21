// Data
var cruise_positions = '{{ cruise_positions }}';
var cruise_polygon = '{{ cruise_polygon }}';
var stations = '{{ station_positions }}';
var crossovers = '{{ crossover_positions }}';
var stations_polygon = '{{ stations_polygon }}'

// Map
var raster = new ol.layer.Tile({
    source: new ol.source.OSM()
});

var features = []
var format = new ol.format.WKT();

var feature = format.readFeature(cruise_positions, {
    dataProjection: 'EPSG:4326',
    featureProjection: 'EPSG:3857'
});
feature.setStyle(blue_hole_map)
// Add all cruise stations as first layer
features.push(feature)


feature = format.readFeature(stations, {
    dataProjection: 'EPSG:4326',
    featureProjection: 'EPSG:3857'
});
feature.setStyle(blue_map)
// Stations filtered by parameter
features.push(feature)

var cross_feature = null
if (crossovers && crossovers != 'None') {
    cross_feature = format.readFeature(crossovers, {
        dataProjection: 'EPSG:4326',
        featureProjection: 'EPSG:3857'
    });
    cross_feature.setStyle(red_map);
    features.push(cross_feature)
}
var buffer_feature = null
if (stations_polygon && stations_polygon != 'None')
  buffer_feature = format.readFeature(stations_polygon, {
    dataProjection: 'EPSG:4326',
    featureProjection: 'EPSG:3857'
  });
  buffer_feature.setStyle(blue_line_map);
  features.push(buffer_feature)

var source = new ol.source.Vector({
    features: features
})
var vector = new ol.layer.Vector({
    source: source
});

var map = new ol.Map({
    layers: [raster, vector],
    target: 'map',
});
map.getView().fit(source.getExtent(), map.getSize())
map.getView().setZoom(map.getView().getZoom() - 1)
