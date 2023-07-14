from flask import Flask
from flask_restful import Api
from resources.pessoa import PessoaResource,PessoasResource
from resources.reserva import ReservaResource,ReservasResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# Inicialização da API
api = Api(app)

#Cria Base de dados na primeira vez em que é executado
@app.before_first_request
def cria_banco():
    banco.create_all()

# Adiciona o recurso "Pessoa" à API
#api.add_resource(PessoasResource, '/pessoas')
#api.add_resource(PessoaResource, '/pessoa/<int:pessoa_id>')
#api.add_resource(ReservaResource, '/reserva/<int:reserva_id>')
# Rotas para o recurso "Pessoa"
app.add_url_rule('/pessoas', view_func=PessoasResource.as_view('pessoa_resource'))
app.add_url_rule('/pessoas/<int:pessoa_id>', view_func=PessoaResource.as_view('pessoa_id_resource'))

# Rotas para o recurso "Reserva"
app.add_url_rule('/reservas', view_func=ReservasResource.as_view('reserva_resource'))
app.add_url_rule('/reservas/<int:reserva_id>', view_func=ReservaResource.as_view('reserva_id_resource'))
if __name__ == '__main__':
    from models.banco import banco
    banco.init_app(app)
    app.run(debug=True)

