# Live Subway

Live Subway is a project to provide real-time visualization of the NYC subways, using the real-time MTA data feeds, written with [Flask](flask.pocoo.org).

API endpoint: http://datamine.mta.info/files/[key]/gtfs


#MTA .proto Files
1. Download: https://developers.google.com/transit/gtfs-realtime/gtfs-realtime.proto
2. Download: http://datamine.mta.info/sites/all/files/pdfs/nyct-subway.proto.txt

# Environment Setup
https://github.com/google/protobuf/releases/tag/v3.1.0  
1. Download: protoc-3.1.0-OS.zip   
2. go into unzipped_file/bin  
3. move protoc binary into $PATH  
4. run `protoc --python_path=WORKING_DIRECTORY gtfs-realtime.proto`  
5. run `protoc --python_path=WORKING_DIRECTORY nyct-subway.proto`
6. create API_KEY.py add line 'key=APIKEY'
7. run `python app.py` and pointer browser to  `localhost:5000` to test success



### Weekly goals
- 10/14/16: Set up rudimentary Flask app and environment, mess around with MTA API

- 10/28/16: Sockets and UI stuff
