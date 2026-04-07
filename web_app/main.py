from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home();
#render_template automatically looks in the /templates folder
return render_template('index.html',title="Home Page")
if__name__=='__main':
#Localo development server
app.run(host='127.0.01',port=8080, debug=True)
