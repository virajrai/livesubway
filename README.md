# Live Subway

Live Subway is a project to provide real-time visualization of the NYC subways, using the real-time MTA data feeds, written with [Flask](flask.pocoo.org).

API endpoint: http://datamine.mta.info/files/[key]/gtfs


# ProtoBuf Download
https://github.com/google/protobuf/releases/tag/v3.1.0  
1. Download: protoc-3.1.0-OS.zip  
2. Unpack  
3. go into unzipped_file/bin  
4. move protoc binary into $PATH  
5. run it  

#MTA Protobuf compilation
1. Download: https://developers.google.com/transit/gtfs-realtime/gtfs-realtime.proto
2. Download: http://datamine.mta.info/sites/all/files/pdfs/nyct-subway.proto.txt
3. run protoc compilation on nyct-subway.proto

### Weekly goals
- 10/14/16: Set up rudimentary Flask app and environment, mess around with MTA API

