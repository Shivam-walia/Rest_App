#%%

MyApp=Flask(__name__)
#blueprint=Blueprint('api',__name__,url_prefix='/api')
api=Api(MyApp)
#%%
@api.route('/Helloworld')
class Helloworld(Resource):
    def get(self):
        return {'Data': 'Hello World'}
   
#%%  
if __name__=='__main__':
    MyApp.run(debug=True)
        
        

        

        
        
        
        
        
        
        
        
