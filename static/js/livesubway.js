
function log(msg){
	console.log(msg);
}

mapboxgl.accessToken="pk.eyJ1Ijoiam9uYXRoYW56aGFuZzk5IiwiYSI6ImNpdjQzMGZjazAwMmsydHJpbW03ZTN4cnEifQ.HD9WQRZXTUG6ygjZ8VWxTg";
var map = new mapboxgl.Map({
	container: "subwaymap",
	style: 'mapbox://styles/mapbox/light-v9',
	//maxBounds: [[-73.995130, 40.79896], [-73.97, 40.76]],
	center: [-73.983393, 40.788552],
	dragRotate: false,
	zoom: 10.84,
});


map.on('load', function () {

	var route_ids = {};
	var color_cnt = 0;
	$.getJSON("/map_json", function(mapdata){
	$.getJSON("/stops_json", function(stopdata){

		$.each( mapdata, function(mapkey, mapval){
			var features = [];
			var srcmap = {};
			var srcstop = {};
			var route_id ="route-".concat(mapkey);
			route_ids[route_id] = 0;
				
			map.addSource(route_id,{
				"type" : "geojson",
				"data" : {
					"type" : "Feature",
					"properties": {
						"color":mapval.color
					},
					"geometry": {
						"type" : "LineString",
						"coordinates" : mapval.points
					}
				}
			});
		});



			//log(route_ids);
		route_ids["route-1..N03R"] = 1;
		route_ids["route-1..N06R"] = 1;

		route_ids_list = ["route-1..N03R",
						  "route-5..S03R", 
						  "route-A..N04R", 
						  "route-N..N20R",
						  "route-D..N05R",
						  "route-B..N46R"
						  ];
		//route_ids["route-1..N05R"] = 1;
		$.each( route_ids_list, function(index, key){
			//if (val === 1){
				log(key);
				log(map.getSource(key));
				map.addLayer({
					"id":key,
					"type":"line",
					"source":key,
					"layout":{
						"line-join": "round",
						"line-cap": "round"
					},
					"paint" : {
						"line-color": map.getSource(key)._data.properties.color,
						"line-width": 3

					}
				});
				color_cnt += 1;	
			//}
		});
		var stops_feature_data = [];
		$.each( stopdata, function(stopkey, stopval){
			var stopid = "stop-".concat(stopkey);
			var descriptionHTML = "<strong>"+stopval.name+"</strong><br><p>[" + stopval.lon + ", " + stopval.lat + "]</p>";
			stop_source = {
				"type": "Feature",
				"properties": {
					"description": descriptionHTML
				},
				"geometry": {
					"type": "Point",
					"coordinates": [stopval.lon, stopval.lat]
				}

			};
			stops_feature_data.push(stop_source);

			

		});
		map.addSource("stops", {
			"type":"geojson",
			"data":{
				"type": "FeatureCollection",
				"features": stops_feature_data
			}
		});
		map.addLayer({
			"id" : "stops",
			"type" : "circle",
			"source": "stops",
			"paint":{
				"circle-radius" : {
					stops:[[11, 3], [14, 4], [16, 5]]
				},
				"circle-color" : "#ff3300"
			}
		});
	
		var point = {
		"type": "FeatureCollection",
		"features" : [{
			"type":"Feature",
			"geometry": {
				"type": "Point",
				"coordinates": [-74.013664, 40.702068]
				}
			}]
		};
		map.addSource("subway_car", {
			"type": "geojson",
			"data": point
		});
		map.addLayer({
			"id":"subway_car",
			"type":"circle",
			"source":"subway_car",
			"paint":{
				"circle-radius" : 4,
				"circle-color" : "#000000"
			}
		});
		var subway_cars = {};
		$.each(route_ids_list, function(key){
			subway_cars["p_"+key] = [];
			
			var src = map.getSource(key);

		});
		var key = route_ids_list[0];
		var src = map.getSource(key);
		var ldistance =  turf.lineDistance(src._data, "miles");
		var timediv = 3000;
		var anim_steps = [];
		for (var i = 0; i < timediv; i++){
			var segment = turf.along(src._data, i /timediv * ldistance, "miles");
			anim_steps.push(segment.geometry.coordinates);
		}	
		log(anim_steps);
		var counter = 0;
		function animate(){
			point.features[0].geometry.coordinates = anim_steps[counter];
			//log(point);
			map.getSource('subway_car').setData(point);

			if (counter < timediv - 1){
				requestAnimationFrame(animate);
			}
			counter = counter + 1;
		}

		animate();

		
	}); // end of stops_json
	}); // end of map_json
	var popup = new mapboxgl.Popup({
		closeButton:false,
		closeOnClick: false
	});


	


	map.on('mousemove', function(e){
		var features = map.queryRenderedFeatures(e.point, {layers: ["stops"]});
		map.getCanvas().style.cursor = (features.length) ? "pointer": "";
		if (!features.length){
			popup.remove();
			return;
		}

		var feature = features[0];
		popup.setLngLat(feature.geometry.coordinates)
		     .setHTML(feature.properties.description)
		     .addTo(map);

	});

});



