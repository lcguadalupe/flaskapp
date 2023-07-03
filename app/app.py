from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "pochu lc"
    return render_template ('home.html', name=name)

@app.route("/3b")
def tres():
    alumnos = ['gaby', 'adriana', 'alicia']
    return render_template('tres.html', alumnos=alumnos)

@app.route ("/contact")
def contact():
    user = "pochu"
    return render_template('contact.html', user=user)

@app.route("/about")
def about():
    user = "pochu"
    return render_template("about.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)
