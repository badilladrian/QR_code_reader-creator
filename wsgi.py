from app import app
from config import *
from app.urls import *
from app.core.models import *

def main():
    app.run(host='0.0.0.0', port=8080, debug=DEBUG)


if __name__ == "__main__":
    main()
