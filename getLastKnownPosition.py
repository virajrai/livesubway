import urllib2
from API_KEY import key
import gtfs_realtime_pb2 as gtfs
import nyct_subway_pb2 as nyct

# demonstrates how to use FeedMessages to get data from API

raw_gtfs = urllib2.urlopen("http://datamine.mta.info/mta_esi.php?key=" +
                           key + "&feed_id=1")
feed = gtfs.FeedMessage()
feed.ParseFromString(raw_gtfs.read())
directionDict = {1: "North", 3: "South"}


def getupdate():
    return feed.entity


def call():
    i = 0
    done = False
    for ii in range(len(feed.entity)):
        entity = feed.entity[ii]
        i += 1
        if done:
            break
        if entity.trip_update.trip.HasExtension(nyct.nyct_trip_descriptor) \
                and (
                    entity.trip_update.
                    trip.Extensions[nyct.nyct_trip_descriptor]
                    .is_assigned):
            print(entity)
            print(feed.entity[ii + 1])
            entity2 = feed.entity[ii + 1]
            stops = []

            print "Trip id:", str(entity.trip_update.trip.trip_id)
            print "Route id:", entity.trip_update.trip.route_id
            print "Current stop number:", \
                entity2.vehicle.current_stop_sequence
            print "Current status:", \
                entity2.vehicle.current_status
            for stop in entity.trip_update.stop_time_update:
                stops.append((stop.stop_id, stop.arrival.time))

            if entity2.vehicle.current_status == 1:
                last_known = stops[0]
            else:
                last_known = None
            print "Last Known Stop:", last_known

            print(stops)
            break
            '''
            haha = None
            for stop in entity.trip_update.stop_time_update:

                if stop.HasExtension(nyct.nyct_stop_time_update):
                    if hasattr(stop.Extensions[nyct.nyct_stop_time_update],
                               'actual_track'):
                        if stop.Extensions[nyct.nyct_stop_time_update].\
                                actual_track != '':
                            print(entity)
                            if i == 2:
                                done = True
                            break
                            haha = stop
            if haha is not None:
                if (haha.Extensions[nyct.nyct_stop_time_update].
                    actual_track
                == '1'):
                    print(haha)
                    print(directionDict[entity.trip_update.trip.Extensions
                    [nyct.nyct_trip_descriptor].direction])
                    '''


call()
