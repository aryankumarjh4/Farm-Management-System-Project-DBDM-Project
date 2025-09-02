from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin, LoginManager, login_user,
    logout_user, login_required, current_user
)

# Application setup
app = Flask(__name__)
app.secret_key = "super_secret_key"  # change this in production

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/farmers"
db = SQLAlchemy(app)

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --------------------
# Database Models
# --------------------
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Farming(db.Model):
    fid = db.Column(db.Integer, primary_key=True)
    farmingtype = db.Column(db.String(100))


class Product(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    productname = db.Column(db.String(100))
    productdesc = db.Column(db.String(300))
    price = db.Column(db.Integer)


class TriggerLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.String(100))
    action = db.Column(db.String(100))
    timestamp = db.Column(db.String(100))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(1000))


class Farmer(db.Model):
    rid = db.Column(db.Integer, primary_key=True)
    farmername = db.Column(db.String(50))
    adharnumber = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    phonenumber = db.Column(db.String(50))
    address = db.Column(db.String(50))
    farming = db.Column(db.String(50))


# --------------------
# Routes
# --------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/farmers")
@login_required
def farmers():
    records = Farmer.query.all()
    return render_template("farmerdetails.html", query=records)


@app.route("/products")
def products():
    items = Product.query.all()
    return render_template("agroproducts.html", query=items)


@app.route("/products/add", methods=["GET", "POST"])
@login_required
def add_product():
    if request.method == "POST":
        data = Product(
            username=request.form.get("username"),
            email=request.form.get("email"),
            productname=request.form.get("productname"),
            productdesc=request.form.get("productdesc"),
            price=request.form.get("price"),
        )
        db.session.add(data)
        db.session.commit()
        flash("Product added successfully", "info")
        return redirect(url_for("products"))
    return render_template("addagroproducts.html")


@app.route("/logs")
@login_required
def logs():
    entries = TriggerLog.query.all()
    return render_template("triggers.html", query=entries)


@app.route("/farming/add", methods=["GET", "POST"])
@login_required
def add_farming():
    if request.method == "POST":
        farming_type = request.form.get("farming")
        if Farming.query.filter_by(farmingtype=farming_type).first():
            flash("This farming type already exists", "warning")
        else:
            new_type = Farming(farmingtype=farming_type)
            db.session.add(new_type)
            db.session.commit()
            flash("Farming type added", "success")
        return redirect(url_for("add_farming"))
    return render_template("farming.html")


@app.route("/farmer/delete/<int:rid>")
@login_required
def delete_farmer(rid):
    record = Farmer.query.get(rid)
    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Farmer deleted successfully", "warning")
    return redirect(url_for("farmers"))


@app.route("/farmer/edit/<int:rid>", methods=["GET", "POST"])
@login_required
def edit_farmer(rid):
    farmer = Farmer.query.get(rid)
    all_farming = Farming.query.all()
    if request.method == "POST":
        farmer.farmername = request.form.get("farmername")
        farmer.adharnumber = request.form.get("adharnumber")
        farmer.age = request.form.get("age")
        farmer.gender = request.form.get("gender")
        farmer.phonenumber = request.form.get("phonenumber")
        farmer.address = request.form.get("address")
        farmer.farming = request.form.get("farmingtype")
        db.session.commit()
        flash("Farmer details updated", "success")
        return redirect(url_for("farmers"))
    return render_template("edit.html", posts=farmer, farming=all_farming)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if User.query.filter_by(email=email).first():
            flash("Email already registered", "warning")
            return render_template("signup.html")

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Signup successful. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            flash("Login successful", "primary")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials", "warning")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
@login_required
def register_farmer():
    farming_types = Farming.query.all()
    if request.method == "POST":
        farmer = Farmer(
            farmername=request.form.get("farmername"),
            adharnumber=request.form.get("adharnumber"),
            age=request.form.get("age"),
            gender=request.form.get("gender"),
            phonenumber=request.form.get("phonenumber"),
            address=request.form.get("address"),
            farming=request.form.get("farmingtype"),
        )
        db.session.add(farmer)
        db.session.commit()
        return redirect(url_for("farmers"))
    return render_template("farmer.html", farming=farming_types)


@app.route("/test")
def test_connection():
    try:
        Test.query.all()
        return "Database connected"
    except Exception:
        return "Database connection failed"


if __name__ == "__main__":
    app.run(debug=True)
