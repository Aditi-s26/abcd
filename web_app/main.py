from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Looks for /templates/index.html
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    # Local execution
    app.run(host='0.0.0.0', port=8080, debug=True)
