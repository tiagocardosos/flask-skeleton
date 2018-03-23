from run import app, JWT
from security import authenticate, identity
jwt = JWT(app, authenticate, identity)
import router


if __name__ == '__main__':
    app.run(debug=True)
