from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def login():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login_submit():
    user_id=request.form.get('user_id','')
    password=request.form.get('password','')
    if user_id =='123' and password =='123':
        return  '<h1 id="result">login successfully</h1>'
    elif user_id =='' and password =='':
        return login()
    else:
        return  '<h1 id="result">login failed</h1>'
if __name__=='__main__':
    app.run(debug=True,port=2200)