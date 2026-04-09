from flask import Flask, render_template
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    # Use the PORT environment variable if available (for Cloud Shell/App Engine)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
