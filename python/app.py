from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/")
def home():
    return """
    <h1>Welcome to My Website!</h1>
    <p>Hi, I am Immadi Manikanta, a Python developer.</p>
    <p>I am a fresh BTech graduate looking for opportunities in IT.</p>
    <a href="/about">Go to About page</a>
    """

@app.route("/about")
def about():
    return "This is Immadi Manikanta's website. I am a Python developer!"

if __name__ == "__main__":
    app.run(debug=True)