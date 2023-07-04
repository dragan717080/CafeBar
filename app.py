from create_app import create_app
from utils import Utils

app = create_app()

for blueprint in Utils.get_blueprints():
    app.register_blueprint(blueprint)

if (__name__ == "__main__"):
    app.run(debug=True)
