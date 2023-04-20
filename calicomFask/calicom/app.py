from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')












@app.route('/<id_name>')
def blog(id_name):
    pages = ['home','products', 'about', 'contact', 'forum', 'blog','services']
    id_name = str(id_name).lower()
    if id_name in pages:
        return redirect("/#" + id_name)
    else:
        return 'Page Not Available'


if __name__ == '__main__':
    app.run()
