import json
from flask import Blueprint, jsonify, request
from marshmallow import Schema, fields
from EDD import lista_doblemente_enlazada


main = Blueprint('main', __name__)
lde = lista_doblemente_enlazada.ListaDobleEnlazada()

# Schemas
class InputSchema(Schema):
    id = fields.Integer(required=True)
    email = fields.Email(required=True)
    name = fields.String(required=True)

input_schema = InputSchema()

class deleteSchema(Schema):
	id = fields.Integer(required=True)

delete_schema = deleteSchema()

# routes
@main.route('/')
def get_data():
		data = lde.imprimir_lista()
		return jsonify({'data': data})


@main.route('/<int:id>')
def get_data_by_id(id):
		try:
			data = lde.buscar(id)
			print(data)
			return jsonify({'data': data})
		except Exception as e:
			return jsonify({'error': str(e)}), 500


@main.route('/add', methods=['POST'])
def post_data():
	try:
			input_data = request.json
			input_schema.load(input_data)
			id = input_data['id']
			email = input_data['email']
			name = input_data['name']
			lde.agregar(id, name, email)
			response = {'data': 'Node created successfully', 'id': id, 'name': name, 'email': email}
			return jsonify(response), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	

@main.route('update', methods=['PUT'])
def put_data():
	try:
		input_data = request.json
		input_schema.load(input_data)
		id = input_data['id']
		email = input_data['email']
		name = input_data['name']
		lde.actualizar(id, name, email)
		response = {'data': 'Node updated successfully', 'id': id, 'name': name, 'email': email}
		return jsonify(response), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
	
@main.route('/delete', methods=['DELETE'])
def delete_data():
	try:
		input_data = request.json
		delete_schema.load(input_data)
		id = input_data['id']
		lde.eliminar(id)
		response = {'data': 'Node deleted successfully', 'id': id}
		return jsonify(response), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@main.route('/grafica', methods=['GET'])
def grafica():
	try:
		lde.imprimir()
		with open("lista.dot", "r") as archivo_dot:
			data = archivo_dot.read()
		return jsonify({'data': data}), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500