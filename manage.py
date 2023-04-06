from app import app, db

from app .urls import *

if __name__ == '__main__':
    app.run(debug=True)