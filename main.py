from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

# display main page
@app.route('/')
def index():
    return render_template('index.html')

# display current bitcoin price
@app.route('/bitcoin')
def bitcoin():
    return "Current bitcoin price"

if __name__ == "__main__":
    app.run()
