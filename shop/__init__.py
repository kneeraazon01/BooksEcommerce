from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "db5821567f7f382d2883960140f805c2da33e9bffd7b78d6"

app = Flask(__name__)
app.secret_key = "db5821567f7f382d28830140f805c2da33e9bffd7b78d6"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
db = SQLAlchemy(app)
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

from flask_admin import Admin

from shop import routes
from shop.models import Books, Purchased_items, Purchases, Reviews, User, Wishlist
from shop.views import AdminView

admin = Admin(app, name="Admin panel", template_mode="bootstrap3")
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Books, db.session))
admin.add_view(AdminView(Reviews, db.session))
admin.add_view(AdminView(Purchases, db.session))
admin.add_view(AdminView(Purchased_items, db.session))
admin.add_view(AdminView(Wishlist, db.session))
