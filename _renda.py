from app import create_app
from app.models import Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'Post':Post}

if __name__ == '__main__':
    app.run(debug=True)
