# Flask allows us to easily set up a server with @app.route()
from flask import Flask, request, jsonify

# This allows us to accept requests from our frontend
# which is on a different server.
from flask_cors import CORS

# Set up the app & tell it (with CORS) that we will allow 
# requests all requests from our frontend
app = Flask(__name__)
CORS(app, resources={r"/hello": {"origins": "*"}})

# This function will be triggered when the server receives a
# POST request at the URL '/hello'
@app.route('/hello', methods=['POST'])
def hello():
  # Grab the name the frontend sends us, which is in the 
  # { 'name': 'your name' } JSON object we are sent in the
  # request
  json = request.json
  name = json['name']

  # Send back a JSON object that has a message object for the
  # frontend to then display.
  return jsonify({ 'message': f'Hello {name}' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
