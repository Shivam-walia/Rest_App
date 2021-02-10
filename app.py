from flask_restplus import Api,Resource
from flask import Flask

app=Flask(__name__)

api=Api(app)

@api.route('/Helloworld')
class Helloworld(Resource):
    def get(self):
        print("Welcome to Flask  Application")
        return ("Data Hello World")
           
if __name__=='__main__':
    app.run(debug=True)
        
        
        
