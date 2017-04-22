from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import sql



app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Cont(db.Model):
    __tablename__ = 'conts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    cont = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime(timezone=True), default=sql.func.now() )

    def __repr__(self):
        return u'<user No:{0} , {1} , {2} >'.format(self.id, self.username, self.cont)

def test():
    co = Cont(username='123',cont='我是谁')
    db.session.add(co)
    print (co)
    db.session.commit()
    print (co)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    print('rebuild database')
    test()