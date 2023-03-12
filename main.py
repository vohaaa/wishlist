from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="vohaa",
    password="V679nwYkjUUpEh!",
    hostname="vohaa.mysql.pythonanywhere-services.com",
    databasename="vohaa$wishlist",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class Wish(db.Model):
    __tablename__ = "wish"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    userId = db.Column(db.Integer)
    description = db.Column(db.String(5000))

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
# def add_wish():
#     print(request)
#     wish = Wish(title=request.data.title, userId=request.data.userId,description=request.data.description)
#     db.session.add(wish)
#     db.session.commit()
def wishlist():
    iwish = Wish.query.all()
    data = {}
    data['data'] = [{title: "klklk"}]
    response = jsonify(data)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/add')
# def add_wish():
#     print(request)
#     wish = Wish(title=request.form.title, userId=request.form.userId,description=request.form.description)
#     db.session.add(wish)
#     db.session.commit()
if __name__=="__main__":
    app.run()