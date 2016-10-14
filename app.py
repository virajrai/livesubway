from flask import Flask
app=Flask(__name__)

@app.route('/')
def test():
	return "TESTING TESTING TESTING"