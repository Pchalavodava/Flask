from app import app


@app.route('/')
def example():
    return "For example Hello"

