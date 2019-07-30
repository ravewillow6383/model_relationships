from config import Config
from app import create_app

app = create_app(Config)

if __name__ == 'main':
    app.run(host='0.0.0.0')