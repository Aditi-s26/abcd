from flask import Flask, render_template_string

app = Flask(__name__)

# This is the HTML template stored as a variable
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: sans-serif; background: #eef2f3; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .box { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); text-align: center; }
        h1 { color: #333; }
        .success { color: #2ecc71; font-weight: bold; }
    </style>
</head>
<body>
    <div class="box">
        <h1>{{ title }}</h1>
        <p class="success">✔ Fixed! No more TemplateNotFound error.</p>
        <p>This version uses <b>render_template_string</b> so it doesn't need a folder.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # We use render_template_string instead of render_template
    return render_template_string(HTML_TEMPLATE, title="Emergency Template")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
