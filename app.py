from feed import FeedTimer
from flask import Flask, json, jsonify, render_template
from flask_socketio import SocketIO
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
socketio = SocketIO(app)
feed_timer = FeedTimer()


@app.route('/')
def index():
    entities = []
    feed = feed_timer.get_feed()
    for entity in feed.entity:
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
    try:
        feed_timer.start()
        socketio.run(app, debug=True)

    finally:
        print "Interrupt received, stopping feed timer..."
        feed_timer.stop()
        print "Feed timer stopped."
