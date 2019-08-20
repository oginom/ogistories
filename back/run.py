from flask import Flask, json, jsonify

from database import init_db

def create_app():
  app = Flask(__name__)
  app.config.from_object('config.Config')
  app.config.from_pyfile('config.py', silent=False)
  init_db(app)
  return app

app = create_app()

@app.route('/api/')
def api():
    return 'API'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
