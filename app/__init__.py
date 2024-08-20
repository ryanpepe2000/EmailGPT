from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Import routes
        from . import routes
        app.register_blueprint(routes.bp)
        # Register Blueprints if you have any
        # from .blueprint import blueprint
        # app.register_blueprint(blueprint)

        return app