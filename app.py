from eventlet import monkey_patch
from flask import Flask, json, jsonify, render_template
from flask_socketio import SocketIO

import feed

monkey_patch()
app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    entities = []
    for entity in feed.current_feed.entity:
        route_id = entity.trip_update.trip.route_id
        vehicle_id = entity.vehicle.trip.route_id
        if ((route_id != "" and route_id == "5") or
           (vehicle_id != "" and vehicle_id == "5")):
            entities.append(entity)

    return render_template("index.html", entities=entities)


@app.route('/map_json')
def map_json():
    return jsonify(json.load(open("test.json")))

if __name__ == "__main__":
    feed_thread = feed.start_timer()
    try:
        socketio.run(app, debug=True)

    finally:
        feed_thread.kill()
