from flask_restplus import Api,Resource
from flask import Flask

MyApp=Flask(__name__)

api=Api(MyApp)

@api.route('/Helloworld')
class Helloworld(Resource):
    def get(self):
        print("Welcome to Flask  Application")
        return ("Data Hello World")
           
if __name__=='__main__':
    MyApp.run(debug=True)
        
        
        
