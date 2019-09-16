# services/users/project/__init__.py

import os
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SEETINGS')
app.config.from_object(app_settings)

# To check that the correct config has been loaded
# print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['get'])
def ping_pong():
    return jsonify({'status': 'success',
                    'message': 'pong!',
                    })