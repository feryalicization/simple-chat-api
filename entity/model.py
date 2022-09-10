from . import db
from datetime import datetime



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    full_name = db.Column(db.String(225))
    username = db.Column(db.String(225))
    email = db.Column(db.String(225), unique=True)
    notlp = db.Column(db.String(225))
    gender = db.Column(db.Integer)
    avatar = db.Column(db.Text)
    password = db.Column(db.String(225))


# class SystemConfig(db.Model):
#     __tablename__ = "system_config"
#     id = db.Column(db.Integer, primary_key=True)
#     begin_date = db.Column(db.DateTime)
#     end_date = db.Column(db.DateTime)
#     created_date = db.Column(db.DateTime)
#     updated_date = db.Column(db.DateTime)
#     deleted_date = db.Column(db.DateTime)
#     created_by = db.Column(db.Integer)
#     updated_by = db.Column(db.Integer)
#     company_id = db.Column(db.Integer)
#     key = db.Column(db.String(255))
#     value = db.Column(db.String(255))



class Chat(db.Model):
    __tablename__ = "chat"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    message = db.Column(db.Text)
    from_id = db.Column(db.Integer)
    to_id = db.Column(db.Integer)
    is_reply = db.Column(db.Boolean, default=False)
    reply_for = db.Column(db.Integer)
    is_reply_message = db.Column(db.Boolean, default=False)

    


