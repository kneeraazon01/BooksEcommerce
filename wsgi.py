from distutils.log import debug
from shop import app as application

if __name__ == "__main__":
    debug = True
    # Add 'debug=True' as parameter on line below to put in debug mode
    application.run()
