from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("login4.html")
database={'Nive':'Nive@123', 'Anbu': 'Anbu@123', 'Subi':'Subi@123'}
@app.route('/form_login',methods=['POST','GET'])
def form_login():
    if request.method=='POST':
        name1=request.form['Username']
        password1=request.form['Password']
        if name1 not in database:
            return render_template('login4.html',info="Invalid User")
        else:
            if database[name1]!=password1:
                return render_template('login4.html',info="Invalid Password")
            else:
                return render_template('home4.html',name=name1)
    return render_template('login4.html')
#main program
if __name__=="__main__":
    app.run(debug=True)
