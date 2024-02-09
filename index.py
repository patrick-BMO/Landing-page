from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<usuario>')
def Home(usuario):
    return render_template('index.html', usuario=usuario)



if __name__ == '__main__':
    app.run(debug=True)