from API_KEY import key
import gtfs_realtime_pb2 as gtfs
import requests
# import nyct_subway_pb2 as nyct

# demonstrates how to use FeedMessages to get data from API

MTA_ENDPOINT = "http://datamine.mta.info/mta_esi.php?key={}&feed_id=1" \
    .format(key)


def get_feed():
    raw_gtfs = requests.get(MTA_ENDPOINT)
    feed = gtfs.FeedMessage()
    feed.ParseFromString(raw_gtfs.content)
    return feed

# testing API usage
# for entity in feed.entity:
#     if (entity.trip_update.trip.HasExtension(nyct.nyct_trip_descriptor)):
#         print entity.trip_update.trip.Extensions[nyct.nyct_trip_descriptor]
