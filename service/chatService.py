import datetime
import json
from sqlalchemy import desc, asc
from flask import jsonify
import sqlalchemy
from entity.model import Chat, User
from entity import db





def Create(param, user_id):
    try:
        if param['flagAction'] == "chat":
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

        
        if param['flagAction'] == "reply":
            create_reply = Chat(
                message=param['message'],
                to_id = param['toId'],
                reply_for = param['chatId'],
                is_reply_message = True,

                #Generate
                created_date=datetime.datetime.now(),
                from_id = user_id,
                created_by=user_id,
            )

            db.session.add(create_reply)
            db.session.commit()

            if create_reply:

                updated = db.session.query(Chat).filter(Chat.id == create_reply.reply_for).first()
                updated.is_reply = True
                db.session.commit()


        return jsonify({'code': '1', 'msg': 'Chat Success Created!'})
    except sqlalchemy.exc.DataError:
        return jsonify({'msg': 'Chat Failed Created!', 'code': '-1'})
    except sqlalchemy.exc.IntegrityError as err:
        return jsonify({'msg': str(err.__cause__), 'code': '-1'})





def chat_list_user(user_id):
    try:
        data = []
        query = db.session.query(User.id.label('userId'), User.full_name)\
            .join(Chat, Chat.to_id == User.id)\
            .filter(Chat.from_id == user_id).group_by(User.id).all()

        for x in query:
            data.append({
                'id': x.userId,
                'fullName': x.full_name,
            })
            

        return jsonify({'code': '1', 'msg': 'Get Data Success!', 'data': data})
    except sqlalchemy.exc.DataError:
        return jsonify({'msg': 'Get Data Failed', 'code': '-1'})
    except sqlalchemy.exc.IntegrityError as err:
        return jsonify({'msg': str(err.__cause__), 'code': '-1'})



def list_conversation(user_id, receiverId):
    try:
        data = []

        query = db.session.query(User.id, Chat.message, Chat.created_date, Chat.id.label('chatId'))\
            .join(Chat, Chat.to_id == User.id)\
            .filter(Chat.from_id == user_id)\
            .filter(Chat.to_id == receiverId).all()

        for x in query:
            data.append({
                'chatId': x.chatId,
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









def reply(user_id):
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


