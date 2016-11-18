import json
import transitfeed



with open("shapes.json", "w") as fin:
    with open("stops.json", "w") as fin2:
        loader = transitfeed.Loader("./static_transit")
        schedule = loader.Load()
        shape_out = {}
        stops_out = {}
        for elem in schedule.GetShapeList():
            shape_out[elem.shape_id] = {}
            shape_out[elem.shape_id]["sequence"] = elem.sequence[-1]
            shape_out[elem.shape_id]["points"] = []
            color = ''
            for route in schedule.GetRouteList():
                if elem.shape_id[0] == route.route_id[0]:
                    color = "#" + route.route_color

            shape_out[elem.shape_id]["color"] = color
            for point in elem.points:
                shape_out[elem.shape_id]["points"].append((point[1], point[0]))
        for stop_object in schedule.GetStopList():
            if stop_object.location_type == 1:
                stops_out[stop_object.stop_id] = {}
                stops_out[stop_object.stop_id]["lon"] = stop_object.stop_lon
                stops_out[stop_object.stop_id]["lat"] = stop_object.stop_lat
                stops_out[stop_object.stop_id]["name"] = stop_object.stop_name
        fin.write(json.dumps(shape_out))
        fin2.write(json.dumps(stops_out))
