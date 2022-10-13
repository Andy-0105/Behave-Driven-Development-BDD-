from flask import Flask, request,render_template
from psutil import STATUS_TRACING_STOP




app = Flask(__name__)
@app.route("/hello/",methods=["GET"])
def home():
    university= request.args.get('university')
    city=request.args.get('city')
    return "hello, "+university+" "+city
if __name__=="__main__":
    app.run(debug=True,port=2200)
