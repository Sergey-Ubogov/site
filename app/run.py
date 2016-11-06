from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def go():
        return render_template("home.html")
@app.route('/gallery')
def go1():
        return render_template("gallery.html")
@app.route('/links')
def go2():
        return render_template("links.html")

if __name__ == "__main__":
    app.run(debug = False, host='0.0.0.0', port=80)
