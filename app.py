from flask import Flask, render_template
import getFeedsTEMP

app = Flask(__name__)


@app.route('/')
def index():
    entities = []
    for entity in getFeedsTEMP.feed.entity:
        route_id = entity.trip_update.trip.route_id
        vehicle_id = entity.vehicle.trip.route_id
        if ((route_id != "" and route_id == "5") or
           (vehicle_id != "" and vehicle_id == "5")):
            entities.append(entity)

    return render_template("index.html", entities=entities)

if __name__ == "__main__":
    app.run(debug=True)
