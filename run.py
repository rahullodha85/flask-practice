import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import  app
from app.user.routes import user


# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

app.register_blueprint(user)

if __name__ == '__main__':
    app.run()