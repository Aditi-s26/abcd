from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():  # Changed semicolon (;) to a colon (:)
    # render_template automatically looks in the /templates folder
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':  # Added missing underscores and fixed 'main'
    # Local development server
    app.run(host='127.0.0.1', port=8080, debug=True) # Fixed the IP address (127.0.0.1)
