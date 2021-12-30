from flask import Flask, render_template, request
from main import pad2pdf

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


# sets Paths
@app.route("/")
def index():
    # Render HTML with count variable
    return render_template("index.html")


@app.route("/generate/", methods = ['POST'])
def generate():

    name = request.form
    numbers = False
    contenttable = False
    comments = False
    if 'numbers' in name:
        numbers= True
    if 'contenttable' in name:
        contenttable = True
    if 'comments' in name:
        comments = True
    pad2pdf(name['pad'], name['style'],".", numbers, contenttable, comments)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
