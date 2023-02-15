import config
from flask_cors import CORS


app = config.connex_app
app.add_api(config.basedir / 'swagger.yml')
CORS(app.app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
