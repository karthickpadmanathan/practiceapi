from flask_restx import Namespace,Resource

auth_namespace=Namespace('auth',description="Namespace for authendication")


@auth_namespace.route('/')
class HelloAuth(Resource):
    
    def get(self):
        return {'message':'Hello Auth'}
    