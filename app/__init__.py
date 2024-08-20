from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import routes
        from . import routes

        # Register Blueprints if you have any
        # from .blueprint import blueprint
        # app.register_blueprint(blueprint)

        return app