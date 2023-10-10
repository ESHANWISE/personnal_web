from flask import render_template,request,abort,redirect,flash,make_response,session,url_for
from sqlalchemy import text

# local imports follows below
from pkg import app,csrf
from pkg.models import db,Post,Registration
from pkg.forms import RegForm





@app.after_request
def after_request(response):
    response.headers["cache-control"]="no-cache, no-store, must-validate"
    return response


# my Preactice
@app.route("/practice/", methods = ["POST","GET"])
def practice():
    if request.method == "GET":
        return render_template('users/practice.html')
    else:
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        if name == '' or pwd == '':
            flash(f'Input fields cannot be empty', category="error")
            flash(f'empty big head cant you read?',category="error")
            return redirect("/practice")
        else:
            allform = f" {name}  {pwd} \n"
            with open('practice.txt','a') as p:
                p.write(allform)
            flash("Form submitted successfully ",category="success")
        return redirect("/practice")


# session

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "GET":#if the method here is POST, for us to retrieve information from users wit method get we do "request.args.get('name of input')"
        return render_template("users/login.html")
    else:
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        if pwd == "1234":
            session["user"]=username #Keep in seession
            return redirect(url_for("dashboard"))
        else:
            return render_template("users/login.html")
        
        
@app.route("/logout")
def logout():
    if session.get("user") != None:
        session.pop("user",None)
        return redirect('/')

#  dashboard 
@app.route("/dashboard")
def dashboard():
    if session.get('user') != None:
        return render_template("users/dashboard.html")
    else:
        flash("YOu must be logged in to view this page")
        return redirect('/login')
# cookies

@app.route("/destination/", methods=["POST","GET"])
def destination():
    if request.method == "GET":
        return render_template('users/destination.html')
    else:
        continent = request.form.get('continent')
        # Keep thee continent inside cokkiees
        flash(f"We wish you a happy time at {continent} ", category="success")
        make = make_response(redirect('/'))
        make.set_cookie("dest",continent)
        return make

@app.route("/tourist_centers/")
def tourist_centers():
    africa = ["Kilimanjoro","Aso rock"]
    europe = ["museum","palace"]
    Asia = ["Citymall"]
#   "This route returns all the tourist_centers in the world
    return render_template("users/tourist_centers.html",africa=africa,europe=europe,Asia=Asia)
  

@app.route("/shops/")
def shops():
    africa = ["Lovetamin","Man Chu"]
    europe = ["Cubana","Orientals"]
    Asia = ["Chiwell"]
#   "This route returns all the tourist_centers in the world
    return render_template("users/shops.html",africa=africa,europe=europe,Asia=Asia)


@app.route('/register',methods=["POST","GET"])
def register():
    reg = RegForm()
    if request.method == "GET":
        return render_template('users/register.html',reg=reg)
    else:
        if reg.validate_on_submit():
            # we will retrieve for data and send to db
            fname = request.form.get('fname')
            lname = request.form.get("lname")
            email = request.form.get("usermail")
            pwd = request.form.get("pwd")
            profile =request.form.get("profile")
            referrer = request.headers.get('Referrer')
            # save to db using ORM insert
            user = Registration(firsname=fname,lastname=lname,email=email,pwd=pwd,profile=profile,extra=referrer)
            db.session.add(user)
            db.session.commit()
            flash(f"Form was submitted by {fname}")
            return redirect("/")
        else:
            return render_template("users/register.html",reg=reg)
    

@app.route("/")
def homepage():
    config_items = app.config
    return render_template('users/home.html',pagename="Home Page",config_items = config_items)


# if we want to exempt any route we omport csrf this exempts csrf protection
@app.route('/submit_contact',methods=["POST","GET"])
@csrf.exempt
def submit_contact():

    name = request.form.get('Fullname')#where name = email on the form
    msg = request.form.get('message')#where name = texts on the form

    if name == "" or msg == "":
        flash("Please complete the fields", category="error")
    else:
        query = f"INSERT INTO feedback set fullname='{name}', message='{msg}'"
        db.session.execute(text(query))
        db.session.commit()

        flash("We will get back to you within 24hrs", category='success')
        flash(f"Thank you {name}, your message was received", category="success")
    return redirect('/')#redirect("/route to redirect")

# @app.route("/")
# def homepage():
#      return render_template('users/index.html')

# @app.route("/layout")
# def layout():
#    return render_template("users/layout1.html")

@app.route('/about' )
def about_us():
    return render_template("users/about.html",pagename="About Us")

@app.route('/blog_post/',methods=["POST","GET"])
@csrf.exempt
def blog_post():
   
    if request.method == "GET":
        return render_template("users/blog_post.html")
    else:
        fname = request.form.get("fullname")
        comments = request.form.get("comment")
        p=Post(post_fullname=fname,post_content = comments)
        db.session.add(p)
        db.session.commit()
        return "done"
