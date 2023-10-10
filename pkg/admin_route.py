from flask import render_template,request,abort,flash,redirect

# local imports follows below
from pkg import app
from pkg.models import Registration,db,Product,Category,Brand


@app.route("/admin/nojoin")
def nojoin():
    """Selecting from multiple tables without joining"""
     # we queried category and have access to product via the relationship
    prod = db.session.query(Product).first()
    # we queried category and have access to product via the relationship
    cat = Category.query.get(2)
    return render_template("admin/nojoin.html",prod=prod,cat=cat)



@app.route("/admin/products")
def all_products():

    # we used this route to learn join
    p = db.session.query(Product).all()#remenber to import product and category
    # control = db.session.query(Product,Category).join(Category).all()
    # join with filter/where
    # control = db.session.query(Product,Category).join(Category).filter(Product.product_price > 10000).all()

    control = db.session.query(Product,Category,Brand).join(Brand).all()
    return render_template("admin/allproducts.html",p=p,control=control)

@app.route("/admin")
def admin_login():
    return "Display login page here"

# updating table
@app.route("/admin/edit/<id>/")
def edit_user(id):
    user = Registration.query.get(id)
    # user.firsname = request.form.get("firsname")
    user.firsname = "Kelvin"
    user.lastname = "ubumtu"
    user.email = "wiseman@gmail.com"
    db.session.commit()
    return redirect("/admin/user/")

# delete user
@app.route("/admin/delete/<int:id>/")
def delete_user(id):
    users = Registration.query.get_or_404(id)
    db.session.delete(users)
    db.session.commit()
    flash("Profile deleted")
    return redirect("/admin/user")

@app.route("/admin/users/<int:id>/")
def show_user(id):
    # fetch the user details method 1
    # details = db.session.query(Registration).get(id)

    # fetch the user details method 2
    details = Registration.query.get_or_404(id)
    return render_template("admin/user_details.html", details=details)

@app.route("/admin/user/")
def users():
# we used this to learn filters/where statements

    # using Orm we want to see all the users in the db


    users = db.session.query(Registration).limit(2)
    # method 1
    # users = db.session.query(Registration).filter(Registration.regid > 2).all()
    # fetchinf from multiple columns filter serves as WHERE clause
#     users = db.session.query(Registration).filter(Registration.regid > 2, Registration.firsname == "PRECIOUS").all()
#     # fetching from individual columns
    users_explore = db.session.query(Registration).filter((Registration.firsname=="PRECIOUS")|(Registration.firsname=="Eniola")).all()
#     # users_explore = db.session.query(Registration.email,Registration.firsname,Registration.lastname).all()
#     #  counting records
    total = db.session.query(Registration).count() 
#     # .or_

# #     user= db.session.query(Registration).filter((Registration.firstname == "Goji")|(Registration.firstname=="Carrington")).all()
# #     user= db.session.query(Registration).filter(db.or_(Registration.firstname == "Goji",Registration.firstname=="Carrington")).all()
#     users=db.session.query(Registration.email,Registration.firsname, Registration.lastname).all()
#     users=db.session.query(Registration).filter(Registration.regid > 1).all()

#     in_
#     user=db.session.query(Registration).filter(Registration.firstname.in_(names)).all()

#    not_in
#     user=db.session.query(Registration).filter(Registration.firstname.not_in(names)).all()
    #method 2

#    like
    users=db.session.query(Registration).filter(Registration.firsname.like('%a%')).all()

    # geting one record
    oneuser = db.session.query(1)

    # method2 in this one, we dont need to import db above
    # users = Registration.query.all()
    return render_template("admin/allusers.html", users=users,users_explore=users_explore,total=total,oneuser=oneuser)