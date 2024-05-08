import os
# from flask import Flask


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')


"""def my_config(app: Flask):
    app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
    app.config["GOOGLE_CLIENT_ID"] = 'YOUR_GOOGLE_CLIENT_ID'
    app.config['GOOGLE_CLIENT_SECRET'] = 'YOUR_GOOGLE_CLIENT_SECRET' """

