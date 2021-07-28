from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

login = LoginManager()
db = SQLAlchemy()


class Admin(UserMixin, db.Model):
    __tablename__ = "login"

    email = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String())
    login_status = db.Column(db.Boolean, default=False)
    token = None

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.email


@login.user_loader
def load_user(email):
    return Admin.query.filter_by(email=email).first()


class Details(db.Model):
    __tablename__ = "Details"
    emp_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    job_grade = db.Column(db.String(100))
    ibm_laptop_status = db.Column(db.Boolean, default=False)
    position_in_ibm = db.Column(db.String(100))
    designation_in_infinite = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=False)
    date_of_joining_infinite = db.Column(db.Date)
    last_working_date = db.Column(db.Date)
    po_no = db.Column(db.Integer, default=False)
    po_start_date = db.Column(db.Date)
    po_end_date = db.Column(db.Date)
    ibm_manager = db.Column(db.String(100))
    account_manager = db.Column(db.String(100))
    ibm_emp_id = db.Column(db.Integer)
    ibm_email_id = db.Column(db.String(100))
    emp_location = db.Column(db.String(100))
    experience = db.Column(db.Integer)
    per_day_rate_dollars = db.Column(db.Float)
    per_day_rate_INR = db.Column(db.Float)
    ctc = db.Column(db.Float)
    ctc_in_dollars = db.Column(db.Float)
    gm_perctange = db.Column(db.Float)
    actual_billing_date = db.Column(db.Date)
    mobile_number = db.Column(db.Integer)
    under_taking_letter = db.Column(db.Boolean, default=False)
    skill_set = db.Column(db.String(200))
    laptop_received_date = db.Column(db.Date)
    address = db.Column(db.String(100))
    ibm_status = db.Column(db.Boolean)
    admin_email = db.Column(db.String(80), db.ForeignKey("login.email"))
