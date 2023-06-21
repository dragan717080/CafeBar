from create_app import create_app
from routing.routes import index_pages
from routing.routes_cafes import cafes_pages
from routing.routes_chas import chas_pages
from routing.routes_emporio import emporio_pages
from routing.routes_aprendamais import aprendamais_pages
from routing.routes_profile import profile_pages
from routing.routes_favorite_items import favorite_items_pages
from routing.routes_cart import cart_pages
from routing.routes_register import register_pages
from routing.routes_logout import logout_pages
from routing.routes_blogs import blogs_pages
from routing.routes_api import api_pages

app = create_app()

app.register_blueprint(index_pages)
app.register_blueprint(cafes_pages)
app.register_blueprint(chas_pages)
app.register_blueprint(emporio_pages)
app.register_blueprint(aprendamais_pages)
app.register_blueprint(profile_pages)
app.register_blueprint(favorite_items_pages)
app.register_blueprint(cart_pages)
app.register_blueprint(register_pages)
app.register_blueprint(logout_pages)
app.register_blueprint(blogs_pages)
app.register_blueprint(api_pages)

if (__name__ == "__main__"):
    app.run(debug=True)