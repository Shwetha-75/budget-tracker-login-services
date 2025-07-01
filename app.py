from flask import Flask,request,jsonify,make_response
import requests
from config import *
import os
from flask_cors import CORS
from implementation.UserValidation import * 
from implementation.UserModelDisplay import *
# configuration is successful 

import dotenv 

dotenv.load_dotenv()

app=Flask(__name__)
userValidation=UserValidation()
CORS(app,supports_credentials=True,resources={r"/*":{"origins":[os.getenv('FRONT_END_URL_2'),os.getenv('FRONT_END_URL_1'),os.getenv('FRONT_END_URL_3')]}})

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_data=dict(request.form) if request.form else request.get_json()
        if userValidation.validateUser(user_data):
            userObject=UserModelDisplay(userValidation.currentUser)
            return jsonify({
                  'user_model':userObject.methodUserObject(),
                  'status':'ok'
            })
        
    return jsonify({"status":"no"})


if __name__=='__main__':
    app.run(host='0.0.0.0',port=os.getenv("PORT"),debug=True)
    