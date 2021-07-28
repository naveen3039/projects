from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_login import login_user, logout_user
from models import Admin, db, login, Details
from config import USER, DATABASE, PASSWORD, HOST
import jwt
import datetime
from functools import wraps


app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "this is my secret key"
db.init_app(app)
login.init_app(app)
login.login_view = "login"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not Admin.token:
            return f'The token is expired \
               <a href={request.url_root} > "Press here for login again"</a>'
        try:
            data = jwt.decode(Admin.token, app.config["SECRET_KEY"], algorithms="HS256")
            user = Admin.query.get(data["email"])
        except jwt.InvalidTokenError:
            return "Invalid token.Please login again"
        except:
            return jsonify({"message": "invalid token"})
        return f(user, *args, **kwargs)

    return decorated


@app.before_first_request
def create_all():
    db.create_all()


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("login.html", url=request.url_root)


@app.route("/reg", methods=["POST", "GET"])
def reg():
    return render_template("register.html", url=request.url_root)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        conform_password = request.form.get("cpassword")
        email = request.form.get("email")
        if password == conform_password:
            if Admin.query.get(email):
                return "Email already Present"
            user = Admin(email=email, username=user)
            user.set_password(conform_password)
            db.session.add(user)
            db.session.commit()
            return "Sucessfully registered"
        else:
            return f'incorrect password \
            <a href={request.url_root}reg > "Press here for register again"</a>'


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = Admin.query.get(email)
        if user is not None:
            if user.check_password(password):
                payload = {
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=20),
                    "iat": datetime.datetime.utcnow(),
                    "email": request.form.get("email"),
                }
                Admin.token = jwt.encode(
                    payload, app.config.get("SECRET_KEY"), algorithm="HS256"
                )
                login_user(user)
                user.login_status = True
                db.session.commit()
                return redirect(url_for("login_sucess"))
            return f'incorrect password \
                <a href={request.url_root} > "Press here for login again"</a>'
        return f'admin not exists please register in  register portal \
                <a href={request.url_root}reg> "Press here for register"</a>'


@app.route(f"/loginsuccess", methods=["POST", "GET"])
@token_required
def login_sucess(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={request.url_root} > "Press here for login again"</a>'
    else:
        return render_template(
            "login_success.html",
            url=request.url_root,
            admin=user.username,
            email=user.email,
        )


@app.route("/logout", methods=["POST", "GET"])
@token_required
def logout(user):
    user.login_status = False
    db.session.commit()
    Admin.token = None
    logout_user()
    return f' You are sucessfully logged out \
            <a href={request.url_root} > "Press here for login again"</a>'


@app.route("/change", methods=["POST", "GET"])
@token_required
def change(user):
    return render_template("changepassword.html", url=request.url_root)


@app.route("/changepassword", methods=["POST", "GET"])
@token_required
def changepassword(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={request.url_root} > "Press here for login again"</a>'
    else:
        password = request.form.get("password")
        newpassword = request.form.get("password1")
        conform_password = request.form.get("pa ssword2")
        if user.check_password(password):
            if newpassword == conform_password:
                if user.check_password(newpassword):
                    return "The new password and old password both are same so failed to change password "
                user.set_password(newpassword)
                db.session.commit()
                Admin.token = None
                user.login_status = False
                logout()
                return "You are Sucessfully changed password  please login again"
            return "You entered password are umatched"
        return "you current password was wrong"


@app.route("/add", methods=["POST", "GET"])
@token_required
def add(user):
    return render_template("add.html", admin_email=user.email, url=request.url_root)


@app.route("/adddetails", methods=["POST"])
@token_required
def adddetails(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={request.url_root} > "Press here for login again"</a>'
    else:
        try:
            details = Details(
                emp_id=request.form.get("EMPID"),
                name=request.form.get("name"),
                email=request.form.get("email"),
                job_grade=request.form.get("Job_Grade"),
                designation_in_infinite=request.form.get("Designation_in_Infinite"),
                status=bool(request.form.get("Status")),
                date_of_joining_infinite=request.form.get("DOJ_Infinite"),
                last_working_date=request.form.get("LWD"),
                emp_location=request.form.get("Emp_Location"),
                po_no=request.form.get("PO_no"),
                po_start_date=request.form.get("PO_start_date"),
                po_end_date=request.form.get("PO_end_date"),
                account_manager=request.form.get("Account_manager"),
                experience=request.form.get("Experience"),
                per_day_rate_dollars=request.form.get("Per_day_rate_dollar"),
                per_day_rate_INR=request.form.get("Per_day_rate_INR"),
                ctc=request.form.get("CTC"),
                ctc_in_dollars=request.form.get("CTC_dollar"),
                actual_billing_date=request.form.get("Actual_billing_date"),
                mobile_number=request.form.get("Mobile_Number"),
                under_taking_letter=bool(request.form.get("Under_taking_letter")),
                skill_set=request.form.get("Skill_set"),
                laptop_received_date=request.form.get("Laptop_received_date"),
                address=request.form.get("Address"),
                ibm_status=bool(request.form.get("IBM")),
                admin_email=request.form.get("admin_email"),
            )
            if request.form.get("IBM") == "True":
                details.ibm_laptop_status = bool(request.form.get("IBM_Laptop_Status"))
                details.position_in_ibm = request.form.get("Position_in_IBM")
                details.ibm_emp_id = request.form.get("IBM_EMP_ID")
                details.ibm_email_id = request.form.get("IBM_Mail_ID")
                details.ibm_manager = request.form.get("IBM_Manager")
                db.session.add(details)
                db.session.commit()
                return "infinite details,ibm details are added"
            db.session.add(details)
            db.session.commit()
            return f"Infinite details are added \
                <a href={request.url_root}/loginsuccess > 'Press here for home page'</a>"
        except:
            return "you entered employee id is already exists or empty"


@app.route("/ibm", methods=["POST", "GET"])
@token_required
def ibm(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={request.url_root} > "Press here for login again"</a>'
    else:
        return render_template("ibm.html", url=request.url_root)


@app.route("/ibmdetails", methods=["POST", "GET"])
@token_required
def ibmdetails(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        id = request.form.get("id")
        employee = Details.query.get(id)
        if employee is not None:
            if str(employee.emp_id) == id:
                employee.ibm_status = True
                employee.ibm_laptop_status = bool(request.form.get("IBM_Laptop_Status"))
                employee.position_in_ibm = request.form.get("Position_in_IBM")
                employee.ibm_emp_id = request.form.get("IBM_EMP_ID")
                employee.ibm_email_id = request.form.get("IBM_Mail_ID")
                employee.ibm_manager = request.form.get("IBM_Manager")
                db.session.commit()
                return f"The ibm details are successfully add to id {id}\
               <a href={request.url_root}/loginsuccess > 'Press here for home page'</a>"
            return "The employee not found\
               <a href={request.url_root}/loginsuccess > 'Press here for home page'</a>"
        return "He was not a Infinite employee "


@app.route("/delete", methods=["POST", "GET"])
@token_required
def delete(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        return render_template("delete.html", url=request.url_root)


@app.route("/deletedetails", methods=["POST", "GET"])
@token_required
def delete_employee(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        id = request.form.get("EMPID")
        if Details.query.get(id):
            Details.query.filter_by(emp_id=id).delete()
            db.session.commit()
            return f"Sucessfully deleted of Employeeid={id}\
                <a href={request.url_root}/loginsuccess > 'Press here for home page'</a>"
        else:
            return "The employee are not exist"


@app.route("/update", methods=["POST", "GET"])
@token_required
def update(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        return render_template(
            "update.html", url=request.url_root, admin_email=user.email
        )


@app.route("/updatedetails", methods=["POST"])
@token_required
def updatedetails(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        id = request.form.get("EMPID")
        if Details.query.get(id):
            details = Details.query.get(id)
            if request.form.get("EMPID"):
                details.emp_id = request.form.get("EMPID")
            if request.form.get("name"):
                details.name = request.form.get("name")
            if request.form.get("email"):
                details.email = request.form.get("email")
            if request.form.get("Job_Grade"):
                details.job_grade = request.form.get("Job_Grade")
            if request.form.get("Designation_in_Infinite"):
                details.designation_in_infinite = request.form.get(
                    "Designation_in_Infinite"
                )
            details.status = bool(request.form.get("Status"))
            if request.form.get("DOJ_Infinite"):
                details.date_of_joining_infinite = request.form.get("DOJ_Infinite")
            if request.form.get("LWD"):
                details.last_working_date = request.form.get("LWD")
            if request.form.get("Emp_Location"):
                details.emp_location = request.form.get("Emp_Location")
            if request.form.get("PO_no"):
                details.po_no = request.form.get("PO_no")
            if request.form.get("PO_start_date"):
                details.po_start_date = request.form.get("PO_start_date")
            if request.form.get("PO_end_date"):
                details.po_end_date = request.form.get("PO_end_date")
            if request.form.get("Account_manager"):
                details.account_manager = request.form.get("Account_manager")
            if request.form.get("Experience"):
                details.experience = request.form.get("Experience")
            if request.form.get("Per_day_rate_dollar"):
                details.per_day_rate_dollars = request.form.get("Per_day_rate_dollar")
            if request.form.get("Per_day_rate_INR"):
                details.per_day_rate_INR = request.form.get("Per_day_rate_INR")
            if request.form.get("CTC"):
                details.ctc = request.form.get("CTC")
            if request.form.get("CTC_dollar"):
                details.ctc_in_dollars = request.form.get("CTC_dollar")
            if request.form.get("Actual_billing_date"):
                details.actual_billing_date = request.form.get("Actual_billing_date")
            if request.form.get("Mobile_Number"):
                details.mobile_number = request.form.get("Mobile_Number")
            details.under_taking_letter = bool(request.form.get("Under_taking_letter"))
            if request.form.get("Skill_set"):
                details.skill_set = request.form.get("Skill_set")
            if request.form.get("Laptop_received_date"):
                details.laptop_received_date = request.form.get("Laptop_received_date")
            if request.form.get("Address"):
                details.address = request.form.get("Address")
            details.ibm_status = bool(request.form.get("IBM"))
            if request.form.get("admin_email"):
                details.admin_email = request.form.get("admin_email")
            if request.form.get("IBM") == "True":
                details.ibm_laptop_status = bool(request.form.get("IBM_Laptop_Status"))
                if request.form.get("Position_in_IBM"):
                    details.position_in_ibm = request.form.get("Position_in_IBM")
                if request.form.get("IBM_EMP_ID"):
                    details.ibm_emp_id = request.form.get("IBM_EMP_ID")
                if request.form.get("IBM_Mail_ID"):
                    details.ibm_email_id = request.form.get("IBM_Mail_ID")
                if request.form.get("IBM_Manager"):
                    details.ibm_manager = request.form.get("IBM_Manager")
                db.session.commit()
                return "infinite details,ibm details are updated\
                <a href={request.url_root}/loginsuccess > 'Press here for home page'</a>"
            db.session.commit()
            return f"infinite details,ibm details are updated\
                <a href={request.url_root}/loginsuccess > 'Press here for home page'</a>"
        else:
            return "The employee are not exist"


@app.route("/view", methods=["POST", "GET"])
@token_required
def view(user):

    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        if Details.query.all():
            return render_template(
                "view.html", url=request.url_root, query=Details.query.all()
            )
        return "There is No Data to view add details"


@app.route("/viewibm", methods=["POST", "GET"])
@token_required
def viewibm(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        if Details.query.all():
            return render_template(
                "viewibm.html", url=request.url_root, query=Details.query.all()
            )
        return "There is No Data to view "


@app.route("/viewresource", methods=["POST", "GET"])
@token_required
def viewresource(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        return render_template("viewresource.html", url=request.url_root)


@app.route("/resource", methods=["POST", "GET"])
@token_required
def resource(user):
    if user.login_status == False:
        return f'The token is expired \
               <a href={url_for(redirect(add))} > "Press here for login again"</a>'
    else:
        id = request.form.get("EMPID")
        resource = Details.query.get(id)
        if resource:
            if resource.status:
                status = "active"
            else:
                status = "In active"
            if resource.under_taking_letter:
                under_taking_letter = "taken"
            else:
                under_taking_letter = "Not taken"
            if resource.ibm_status:
                ibm_status = "Selected"
            else:
                ibm_status = "Not selected"
            if resource.ibm_laptop_status:
                ibm_laptop_status = "taken"
            else:
                ibm_laptop_status = "Not taken"
            if resource.ibm_status:
                return jsonify(
                    {
                        "employee id": resource.emp_id,
                        "Name": resource.name,
                        "Email": resource.email,
                        "Job Grade": resource.job_grade,
                        "Position in infinite": resource.designation_in_infinite,
                        "ibm status": ibm_status,
                        "ibm employee id": resource.ibm_emp_id,
                        "ibm email id": resource.ibm_email_id,
                        "ibm manager": resource.ibm_manager,
                        "ibm laptop status": ibm_laptop_status,
                        "status": status,
                        "Date of joining": resource.date_of_joining_infinite,
                        "Last working date": resource.last_working_date,
                        "po no": resource.po_no,
                        "po start date": resource.po_start_date,
                        "po end date": resource.po_end_date,
                        "account manager": resource.account_manager,
                        "employee location": resource.emp_location,
                        "Experience": resource.experience,
                        "Per day rate in $": resource.per_day_rate_dollars,
                        "Per day rate INR ": resource.per_day_rate_INR,
                        "CTC in INR": resource.ctc,
                        "CTC in Dollars": resource.ctc_in_dollars,
                        "GM%": resource.gm_perctange,
                        "Actual billing date": resource.actual_billing_date,
                        "Mobile Number": resource.mobile_number,
                        "Under taking letter": under_taking_letter,
                        "Skill_set": resource.skill_set,
                        "Laptop received date": resource.laptop_received_date,
                        "Address": resource.address,
                    }
                )
            else:
                return jsonify(
                    {
                        "employee id": resource.emp_id,
                        "Name": resource.name,
                        "Email": resource.email,
                        "Job Grade": resource.job_grade,
                        "Position in infinite": resource.designation_in_infinite,
                        "status": status,
                        "ibm status": ibm_status,
                        "Date of joining": resource.date_of_joining_infinite,
                        "Last working date": resource.last_working_date,
                        "po no": resource.po_no,
                        "po start date": resource.po_start_date,
                        "po end date": resource.po_end_date,
                        "account manager": resource.account_manager,
                        "employee location": resource.emp_location,
                        "Experience": resource.experience,
                        "Per day rate in $": resource.per_day_rate_dollars,
                        "Per day rate INR ": resource.per_day_rate_INR,
                        "CTC in INR": resource.ctc,
                        "CTC in Dollars": resource.ctc_in_dollars,
                        "GM%": resource.gm_perctange,
                        "Actual billing date": resource.actual_billing_date,
                        "Mobile Number": resource.mobile_number,
                        "Under taking letter": under_taking_letter,
                        "Skill_set": resource.skill_set,
                        "Laptop received date": resource.laptop_received_date,
                        "Address": resource.address,
                    }
                )
        else:
            return "The employee are not exist"


@app.route("/reset", methods=["POST", "GET"])
def reset():
    return render_template("reset.html", url=request.url_root)


@app.route("/resetpassword", methods=["POST", "GET"])
def resetpassword():
    email = request.form.get("email")
    user = Admin.query.get(email)
    if user:
        return render_template("resetpassword.html", url=request.url_root, email=email)
    return "Admin email is not found"


@app.route("/newpassword", methods=["POST", "GET"])
def newpassword():
    email = request.form.get("email")
    user = Admin.query.get(email)
    password = request.form.get("password")
    newpassword = request.form.get("password1")
    conform_password = request.form.get("password2")
    if user.check_password(password):
        if newpassword == conform_password:
            if user.check_password(newpassword):
                return "The new password and old password both are same so failed to change password "
            user.set_password(newpassword)
            db.session.commit()
            return "You are Sucessfully changed password please login again"
        return "You entered password are umatched"
    return "you current password was wrong"


if __name__ == "__main__":
    app.run(debug=True, port=5003)
