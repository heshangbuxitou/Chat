from flask import Flask
from flask import current_app
from flask import request,url_for
from flask import render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from msg import Cont,db,app
import cgi
import json

# app = Flask(__name__)


def cont_dict(msg):
    return {
        'username':cgi.escape(msg.username),
        'content':cgi.escape(msg.cont),
        'id':msg.id,
        'datetime':msg.timestamp.strftime('%a, %b %d %H:%M')
    }

@app.before_first_request
def i_init():
    pass

@app.route('/chat')
def index():
    if request.args.get('m'):
        cont = request.args.get('m')
        username = request.args.get('username')
        co = Cont(username=username,cont=cont)
        db.session.add(co)
        db.session.commit()
        print (co)
        return json.dumps([]),200
    elif request.args.get('maxID'):
        maxID = int(request.args.get('maxID'))
        conts_lists = Cont.query.filter(Cont.id>maxID).all()
        if len(conts_lists)>50:
            conts_lists = conts_lists[-50:]
        print(conts_lists)
        dict_lists = list()
        for cont_list in conts_lists:
                dict_lists.append(cont_dict(cont_list))
        return json.dumps(dict_lists),200
    else:
        return json.dumps([]),200

@app.route('/user')
def user():
    if not request.args.get('username') or request.args.get('username')=='' :
        return render_template('index.html'),200
    username = request.args.get('username')
    return render_template('char_room.html',username = username),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

