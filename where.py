from config import DEBUG
from core import app
from core.utils import check_static_location_files

if __name__ == '__main__':
    check_static_location_files()
    app.run(debug=DEBUG)
