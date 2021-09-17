from .db import db

class User(db.Document):
    user_name = db.StringField(required=True)
    user_email = db.StringField(required=True)
    user_imgs = db.StringField(required=False)
