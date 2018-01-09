from flask import Flask, render_template, request
app = Flask(__name__)

# display main page
@app.route('/')
def info():
    return "Crypto Tool"

if __name__ == "__main__":
    app.run()
