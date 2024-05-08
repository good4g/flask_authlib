from flask import Flask
from authlib.integrations.flask_client import OAuth

import config
import views
# from config import my_config


app = Flask(__name__)
# my_config(app)
app.config.from_object(config.Config)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)

oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    },
    client_id=app.config["GOOGLE_CLIENT_ID"],
    google_client_secret=app.config["GOOGLE_CLIENT_SECRET"]
)


if __name__ == '__main__':
    app.register_blueprint(views.bp)
    app.run(host='127.0.0.1', port=5000, debug=True)