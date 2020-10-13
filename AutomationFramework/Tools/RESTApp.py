'''
Launches sample RESTful API application
'''

from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

USER_DATA = {
        "Nemuadmin": "nemuuser"
    }

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

put_post_args = reqparse.RequestParser()
put_post_args.add_argument("first_name", type = str, help = "First name is required", required = True)
put_post_args.add_argument("last_name", type = str, help = "Last name is required", required = True)
put_post_args.add_argument("alias", type = str, help = "Alias is required", required = True)
put_post_args.add_argument("sex", type = str, help = "Sex is required", required = True)
put_post_args.add_argument("state", type = str, help = "State is required", required = True)
put_post_args.add_argument("country", type = str, help = "Country is required", required = True)

update_patch_args = reqparse.RequestParser()
update_patch_args.add_argument("first_name", type = str, help = "First name is required")
update_patch_args.add_argument("last_name", type = str, help = "Last name is required")
update_patch_args.add_argument("alias", type = str, help = "Alias is required")
update_patch_args.add_argument("sex", type = str, help = "Sex is required")
update_patch_args.add_argument("state", type = str, help = "State is required")
update_patch_args.add_argument("country", type = str, help = "Country is required")

record = {
    "tony": {
        "first_name": "Anthony Edward",
        "last_name": "Stark",
        "alias": "Ironman",
        "sex": "Male",
        "state": "New York",
        "country": "America"
        },
    "steve": {
        "first_name": "Steven Grant",
        "last_name": "Rogers",
        "alias": "Captain America",
        "sex": "Male",
        "state": "New York",
        "country": "America"
        },
    "thor": {
        "first_name": "Thor",
        "last_name": "Odinson",
        "alias": "Thor",
        "sex": "Male",
        "state": "Asgard",
        "country": "Asgard"
        }
    }

class AppInfo(Resource):
    @auth.login_required
    def get(self):
        return {"data": "AppInfo"} 

class EchoParam(Resource):
    @auth.login_required
    def get(self, param):
        return {"param": param}
   
class Record(Resource):
    @auth.login_required
    def get(self, name):
        '''
        Returns a given record identified by its name
        '''
        if name not in record:
            return "[404] Record not found"
        else:
            return record[name]
    
    @auth.login_required
    def put(self, name):
        '''
        Adds a new record given by name to record dictionary
        '''
        args = put_post_args.parse_args()
        record[name] = args
        return record[name], 201    #created
    
    @auth.login_required
    def post(self, name):
        '''
        Adds a new record given by name to record dictionary
        '''
        args = put_post_args.parse_args()
        record[name] = args
        return record[name], 201    #created
    
    @auth.login_required
    def delete(self, name):
        '''
        Deletes an existing record
        '''
        if name not in record:
            return "[409] Record does not exist"
        else:
            del record[name]
            return {}, 204          #deleted
        
    @auth.login_required    
    def patch(self, name):
        '''
        Patches an existing record given by name
        '''
        args = update_patch_args.parse_args()
        print(args)
        for key in args.keys():
            if args[key] != None:
                record[name][key] = args[key]
        
        return record[name]
    
class Records(Resource):
    @auth.login_required
    def get(self):
        '''
        Returns all records
        '''
        return record

#Add endpoints from classes created
api.add_resource(AppInfo, "/appinfo")
api.add_resource(EchoParam, "/echoparam/<string:param>")
api.add_resource(Record, "/record/<string:name>")
api.add_resource(Records, "/records")

if __name__ == "__main__":
    app.run(debug = True)