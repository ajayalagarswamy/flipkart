from flask import Flask,redirect,render_template,request,session,url_for
import sqlite3 as sql


app=Flask(__name__)

app.secret_key = "ajay"


@app.route("/")
def home():
    conn=sql.connect("user.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from buyer")
    data=cur.fetchall()
    return render_template("index.html",datas=data)


@app.route("/fashion",methods=["POST","GET"])
def fashion():
    if request.method=="POST":
        data=request.json
        conn=sql.connect("user.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("insert into seller(image,product_name,description,price,quantity) values(?,?,?,?,?)",
                    (data["image"],data["product_name"],data["description"],data["price"],data["quantity"]))
        conn.commit()

    conn=sql.connect("user.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from buyer")
    data1=cur.fetchall()
    return render_template("fashion.html",datas=data1)



@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        conn = sql.connect('user.db')
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('select  *  from  login  where email=?',(email,))
        data = cur.fetchone()
        if data:
            if str(data['email']) == str(email)  and   str(data['password']) == str(password):
                session['email'] =data['email']
                return render_template('index.html',data=data)
        else:
            return  'user not exist'
    return render_template('login.html')


@app.route('/api',methods=["POST","GET"])
def api():
    if request.method=="POST":
        s=request.json
        conn=sql.connect('user.db')
        conn.row_factory = sql.Row
        cur=conn.cursor()
        cur.execute("insert into buyer(image,price,description,product_name,quantity) values(?,?,?,?,?)",
                    (s['image'],s['price'],s['description'],s['product_name'],s['quantity']))
        conn.commit()
        print(s)
        return redirect(url_for("home"))
    conn=sql.connect("user.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from buyer")
    data=cur.fetchall()
    return render_template("fashion.html",datas=data)


    

@app.route('/logout')
def logout():
    session.pop(None,"name")
    return redirect(url_for('home'))



@app.route('/signup',methods= ['POST','GET'])
def signup():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        conn = sql.connect('user.db')
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('insert into login(name,email,password)  values(?,?,?)',(name,email,password))
        conn.commit()
        return redirect(url_for('home'))
    return render_template('signup.html')



if __name__ == "__main__":
    app.run(debug=True,port=5000)