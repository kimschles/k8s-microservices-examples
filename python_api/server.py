from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes


# Load data from JSON file
with open('data.json') as file:
    learning_resources = json.load(file)

# GET /learning_resources
@app.route('/', methods=['GET'])
def get_learning_resources():
    return jsonify(learning_resources)


# TODO: Fix these routes!
# # GET /learning_resources/<id>
# @app.route('/learning_resources/<int:learning_resource_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((book for book in learning_resources if book['id'] == book_id), None)
#     if book:
#         return jsonify(book)
#     else:
#         return jsonify({"error": "Book not found"}), 404

# # POST /learning_resources
# @app.route('/learning_resources', methods=['POST'])
# def add_book():
#     new_book = request.get_json()
#     learning_resources.append(new_book)
#     return jsonify(new_book), 201

# # PUT /learning_resources/<id>
# @app.route('/learning_resources/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     book = next((book for book in learning_resources if book['id'] == book_id), None)
#     if book:
#         book.update(request.get_json())
#         return jsonify(book)
#     else:
#         return jsonify({"error": "Book not found"}), 404

# # DELETE /learning_resources/<id>
# @app.route('/learning_resources/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     book = next((book for book in learning_resources if book['id'] == book_id), None)
#     if book:
#         learning_resources.remove(book)
#         return jsonify({"message": "Book deleted"})
#     else:
#         return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)