from flask import Flask
from flask_restful import Api
from resources.pessoa import PessoasResource, PessoaResource
from models.banco import banco
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
CORS(app)

banco.init_app(app)

# Registre os recursos da API
api.add_resource(PessoasResource, '/pessoas')
api.add_resource(PessoaResource, '/pessoa/<int:pessoa_id>')

if __name__ == '__main__':
    with app.app_context():
        banco.create_all()
    app.run()
