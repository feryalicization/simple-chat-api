import datetime
import json
from sqlalchemy import desc, asc
from flask import jsonify
import sqlalchemy
from entity.model import Chat, User
from entity import db





def Create(param, user_id):
    try:
        create = Chat(
            message=param['message'],
            to_id = param['toId'],

            #Generate
            created_date=datetime.datetime.now(),
            from_id = user_id,
            created_by=user_id,
        )

        db.session.add(create)
        db.session.commit()
        return jsonify({'code': '1', 'msg': 'Chat Success Created!'})
    except sqlalchemy.exc.DataError:
        return jsonify({'msg': 'Chat Failed Created!', 'code': '-1'})
    except sqlalchemy.exc.IntegrityError as err:
        return jsonify({'msg': str(err.__cause__), 'code': '-1'})





def chat_list_user(user_id):
    data = []
    query = db.session.query(User.id.label('userId'), User.full_name)\
        .join(Chat, Chat.to_id == User.id)\
        .filter(Chat.from_id == user_id).group_by(User.id).all()

    for x in query:
        data.append({
            'id': x.userId,
            'fullName': x.full_name,
        })

    return data



def list_conversation(user_id):
    try:
        data = []
        query = db.session.query(User.id, Chat.message, Chat.created_date)\
            .join(Chat, Chat.to_id == User.id)\
            .filter(Chat.from_id == user_id)\
            .filter(Chat.to_id == 2).all()

        for x in query:
            data.append({
                'message': x.message,
                'createDate': x.created_date.strftime("%Y-%m-%d %H:%M:%S")
            })

            response = {
                'id': x.id,
                'chat': data}

        return jsonify({'code': '1', 'msg': 'Get Data Success!', 'data': response})
    except sqlalchemy.exc.DataError:
        return jsonify({'msg': 'Get Data Failed', 'code': '-1'})
    except sqlalchemy.exc.IntegrityError as err:
        return jsonify({'msg': str(err.__cause__), 'code': '-1'})

