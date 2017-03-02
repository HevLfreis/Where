from main import app
from main.utils import check_static_location_files

if __name__ == '__main__':
    check_static_location_files()
    app.run(debug=True)
