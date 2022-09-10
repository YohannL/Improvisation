from flask import Flask, render_template

WebApp=Flask(__name__)
WebDbg=True
WebPort=5003
WebHost='0.0.0.0'

@WebApp.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    WebApp.run(debug=WebDbg, port=WebPort ,host=WebHost)