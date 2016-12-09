# Live Subway

Live Subway is a project to provide real-time visualization of the NYC subways, using the real-time MTA data feeds, written with [Flask](flask.pocoo.org).

API endpoint: http://datamine.mta.info/files/[key]/gtfs


# MTA .proto Files
1. Download: [Google GTFS Realtime Proto](https://developers.google.com/transit/gtfs-realtime/gtfs-realtime.proto)
2. Download: [MTA Subway Proto](http://datamine.mta.info/sites/all/files/pdfs/nyct-subway.proto.txt) (remove the `.txt` extension)

# Environment Setup
1. Download: `protoc-[version]-[OS].zip` from the list of [latest Protobuf releases](https://github.com/google/protobuf/releases/latest).   
2. go into `[unzipped_dir]/bin`
3. move protoc binary into $PATH
4. run `protoc --python_path=[WORKING_DIRECTORY] gtfs-realtime.proto`  
5. run `protoc --python_path=[WORKING_DIRECTORY] nyct-subway.proto`  
6. create `API_KEY.py` add the line `key = APIKEY`  
7. create a `static_transit` directory in root directory and add the static `.txt` files there 
8. run `python scripts/static_to_json.py`  
9. run `python app.py` and point browser to  `localhost:5000` to test success  



### Weekly goals
- 10/14/16: Set up rudimentary Flask app and environment, mess around with MTA API
- 10/28/16: Sockets and UI stuff
