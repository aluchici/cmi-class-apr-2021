# class A:
#     def __init__(self):
#         self.__a = None 

#     def set_a(self, a):
#         self.__a = a

#     def get_a(self, a):
#         if self.__check_a():
#             return '404: A is not found'
#         return self.__a

#     def delete_a(self):
#         self.__a = None

#     def update_a(self, a):
#         self.__a = a 

#     def __check_a(self):
#         return self.__a == None
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = []

class Todo(Resource):
    def get(self, todo_id):
        return {'todo': todos[int(todo_id)]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data']

    
api.add_resource(Todo, '/<string:todo_id>')

if __name__ == "__main__":
    app.run(debug=True, port=8888)