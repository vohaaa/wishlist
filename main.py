from flask import Flask,jsonify
import json
app = Flask(__name__)

@app.route('/')
def wishlist():
    iwish = [{
        'id':'29129128',
        'userId':'12',
        'title':'loh',
        'like':'13',
        'pictures':'',
        'links':'https://russianblogs.com/article/43601055383/',
        'description':'очень крутая штука!'
    }]
    data = {}
    data['data'] = iwish
    return jsonify(data)
if __name__=="__main__":
    app.run()