from flask import Flask
from .extensions import login_manager, db, migrate
from .auth.views import auth_bp
from .auth.models import User
from .dashboard.views import dashboard_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)
    # Initialize the database       
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    return app