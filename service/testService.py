from entity.model import User
from entity import db


def List():
    data = []
    query = db.session.query(User).filter(
        User.deleted_date == None).all()

    for x in query:
        data.append({
            'id': x.id,
            'username': x.username,
            'password': x.password,
        })

    return data