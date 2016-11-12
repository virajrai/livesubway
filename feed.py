import threading
from time import sleep

from API_KEY import key
import gtfs_realtime_pb2 as gtfs
# import nyct_subway_pb2 as nyct

import requests

MTA_ENDPOINT = "http://datamine.mta.info/mta_esi.php?key={}&feed_id=1" \
    .format(key)


class FeedTimer(threading.Thread):
    def __init__(self, wait=30):
        print "Creating feed timer..."
        threading.Thread.__init__(self)
        self._wait = wait
        self._kill = threading.Event()
        self._feed = None

    def _get_feed(self):
        print "Retrieving feed..."
        raw_gtfs = requests.get(MTA_ENDPOINT)
        feed = gtfs.FeedMessage()
        feed.ParseFromString(raw_gtfs.content)
        self._feed = feed

    def set_wait(self, wait):
        self._wait = wait

    def get_feed(self):
        return self._feed

    def run(self):
        while not self._kill.is_set():
            self._get_feed()
            sleep(self._wait)

    def stop(self):
        self._kill.set()

# testing API usage
# for entity in feed.entity:
#     if (entity.trip_update.trip.HasExtension(nyct.nyct_trip_descriptor)):
#         print entity.trip_update.trip.Extensions[nyct.nyct_trip_descriptor]
