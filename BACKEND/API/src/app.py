from routes import lde, matriz
from flask import Flask
from flask_cors import CORS

from config import config

app = Flask(__name__)

# Routes

def page_not_found(error):
    return "Page not found", 404


if __name__ == '__main__':

    cors = CORS(app, resources={r"*": {"origins": "*"}})
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(lde.main, url_prefix='/api_lde')
    app.register_blueprint(matriz.m, url_prefix='/api_matriz')
	
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host='localhost', port=8000)
