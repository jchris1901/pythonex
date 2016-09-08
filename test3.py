from flask import Flask,request,url_for,render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('index.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)