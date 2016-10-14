import urllib2
import gtfs_realtime_pb2 as gtfs
import nyct_subway_pb2 as nyct

# demonstrates how to use FeedMessages to get data from API

raw_gtfs = urllib2.urlopen("http://datamine.mta.info/mta_esi.php?key=dd1fb668977d0592c7b26d9fd3b9ca2d&feed_id=1")
feed = gtfs.FeedMessage()
feed.ParseFromString(raw_gtfs.read())

for entity in feed.entity:
	print entity

