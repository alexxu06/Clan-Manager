from app import app

@app.route("/")
@app.route("/index")
def index():
    player = {"username: Female Dog"}
    return "Hello World"