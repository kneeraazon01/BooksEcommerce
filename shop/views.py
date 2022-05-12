from flask_admin.contrib.sqla import ModelView
import flask_login as login
from shop.models import User


class AdminView(ModelView):
    pass


# def is_accessible(self):
#     if login.current_user.is_authenticated:
#         return login.current_user.is_admin
#     return False
