from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def HomePage():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)