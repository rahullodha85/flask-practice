import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import  app
from app.user.routes import user_controller


# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

app.register_blueprint(user_controller, url_prefix ='/user')


@app.route('/')
def index():
    return 'Home Page!'

if __name__ == '__main__':
    app.run()