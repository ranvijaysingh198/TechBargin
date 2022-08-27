# import bcrypt
# from flask import flash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads

import os
from flask_msearch import Search
from pdfkit.api import configuration
from werkzeug.utils import send_file
from flask_login import LoginManager

# import pdfkit

from flask_migrate import Migrate, migrate


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = 'AQSWDEFRGTHYSDFGSDF'

app.config['UPLOADED_PHOTOS_DEST']= os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
# patch_request_class(app)

# config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
# pdfkit.from_string("http://localhost:5000/get_pdf/5ebb9cdfbd", 'MyPDF.pdf', configuration=config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

search = Search()
search.init_app(app)

migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'customerLogin'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = u'Please Login First'


from shop.admin import routes
from shop.products import routes
from shop.carts import carts
from shop.customers import routes