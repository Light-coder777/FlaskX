from flask import Flask
from flask_restful import Api , Resource
app = Flask(__name__)
api = Api(app)

class Hellowrold(Resource):
  def get(self):
    return{"data":"Hello World"}

  def post(self):
    return {"data":"Hello world"}

api.add_resource(Hellowrold,"/helloworld")
if __name__ == "__main__":
  app.run(debug = True)