from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'lightbridge'

  from .view import view
  app.register_blueprint(view, url_prefix='/')

  from .sec1view import sec1view
  app.register_blueprint(sec1view, url_prefix='/')

  return app