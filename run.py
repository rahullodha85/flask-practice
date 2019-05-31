import os

from app import create_app
from app.user.routes import user

config_name = os.getenv('ENV')
app = create_app(config_name=config_name)

app.register_blueprint(user)

if __name__ == '__main__':
    app.run()