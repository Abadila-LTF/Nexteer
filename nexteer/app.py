from flask import Flask ,session ,render_template, flash, request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length


app = Flask(__name__)
# Config
app.secret_key="abadildfa"
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"
# local host 
userpass = 'mysql+pymysql://root:@'
basedir  = '127.0.0.1'
dbname   = '/our_users'
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Models
class Users(db.Model):	
	id_user = db.Column(db.Integer, primary_key = True , autoincrement=True)
	name = db.Column(db.String(80),nullable= False)
	password =db.Column(db.String(30),nullable= False)
	line = db.Column(db.Integer,nullable= False)
	zone = db.Column(db.String(80),nullable= False)

class Logistic(db.Model):	
	__tablename__ = 'logistic'
	id_Logistic = db.Column(db.Integer, primary_key = True , autoincrement=True)
	name = db.Column(db.String(80),nullable= False)
	password =db.Column(db.String(30),nullable= False)


class Half_shift_ref(db.Model):	
	__tablename__ = 'half_shift_ref'
	id_hs_ref = db.Column(db.Integer, primary_key = True , autoincrement=True)


class Eps_reff(db.Model):	
	__tablename__ = 'eps_reff'
	id_eps_ref = db.Column(db.Integer, primary_key = True , autoincrement=True)


class Current_reff(db.Model):	
	__tablename__ = 'current_reff'
	id = db.Column(db.Integer , primary_key=True, autoincrement=True)
	id_user = db.Column(db.Integer)
	id_ref = db.Column(db.Integer)

class Change_his(db.Model):	
	__tablename__ = 'Change_his'
	id = db.Column(db.Integer , primary_key=True, autoincrement=True)
	id_user = db.Column(db.Integer, primary_key = True )
	line = db.Column(db.String(30))
	old_ref_id = db.Column(db.Integer, primary_key = True )
	new_ref_id = db.Column(db.Integer, primary_key = True )
	date_changed = db.Column(db.DateTime, default=datetime.utcnow)

# Forms
class Login(FlaskForm):
	name = StringField("Enter Your Name", validators=[DataRequired()])
	password = PasswordField("Enter Your Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

class chose_ref(FlaskForm):	
	id = StringField("", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Route /
@app.route("/")
def root():
	return redirect(url_for('home'))

# Route /home
@app.route("/home")
def home():
	return render_template("index.html")

# Route /login
@app.route("/login",methods=["POST","GET"])
def login():
	form=Login()
	if form.validate_on_submit():
		name=form.name.data
		password=form.password.data
		form.name.data=''
		form.password.data = ''
		session.permanent =True
		logistic_user = Logistic.query.filter_by(name=name).first()
		if logistic_user is not None :
			if logistic_user.password == password:
				session["user_id"] = logistic_user.id_Logistic
				session["user_name"] = logistic_user.name
				session["user_password"] = logistic_user.password
				return redirect(url_for('logistic')) 
			else :	
				return render_template("login.html", form=form,state=True)
		user = Users.query.filter_by(name=name).first()
		if user is None :
			return render_template("login.html", form=form,state=True)
		if user.password == password:
			session["user_id"] = user.id_user
			session["user_name"] = user.name
			session["user_password"] = user.password
			session["user_line"] = user.line
			session["user_zone"] = user.zone
			return redirect(url_for("line"))
		else :
			return render_template("login.html", form=form,state=True)
	else:
		return render_template("login.html", form=form,state=False)

# Route /line  'Production Chefs'
@app.route("/line",methods=["POST","GET"])
def line():
	form_change = chose_ref()
	form = chose_ref()
	if session["user_line"] == 1 :
		line="EPS"
	else:
		line="Half Shaft"
	if form.validate_on_submit():
		id_cheff = form.id.data
		form.id.data = ''
		if session["user_line"] == 1 :
			ref = Eps_reff.query.filter_by(id_eps_ref=id_cheff).first()
		else : 
			ref = Half_shift_ref.query.filter_by(id_hs_ref=id_cheff).first()
		if ref is None:	
			return redirect(url_for("line"))
		usrid=session["user_id"]
		session["user_cuurent_ref"] = id_cheff
		cr= Current_reff(id_user=usrid , id_ref=id_cheff)
		db.session.add(cr)
		db.session.commit()
		if session["user_line"]==1:
			idref = ref.id_eps_ref
		else :
			idref = ref.id_hs_ref
		return render_template("production.html",abadila=True,wrong_ref=False,form_change=form_change,form=form,ref =idref,line=line,zone=session["user_zone"],name=session["user_name"])
	else:
		return render_template("production.html",abadila =False,wrong_ref=False,form_change=form_change,form=form,line=line,zone=session["user_zone"],name=session["user_name"])
	
# Route /logistic	'Logistic Chefs'
@app.route("/logistic",methods=["POST","GET"])
def logistic():
	currentusers = Current_reff.query.all()
	history = Change_his.query.all()
	l=[]
	if currentusers :
		j=0
		for i in currentusers :
			l.append([])
			chef = Users.query.filter_by(id_user=i.id_user).first()
			if chef.line == 1 :
				l[j].append("EPS")
			else:
				l[j].append("Half shaft")
			
			l[j].append(chef.zone)
			l[j].append(chef.name)	
			l[j].append(i.id_ref)
			j+=1
		for i in l :
			if  i[0] == "EPS":
				reff = Eps_reff.query.filter_by(id_eps_ref=i[3]).first()
				i[3]=reff.id_eps_ref
			elif i[0] == "Half shaft":
				reff = Half_shift_ref.query.filter_by(id_hs_ref=i[3]).first()
				i[3]=reff.id_hs_ref
			else :
				continue
	e=[]
	if history :
		r=0
		for i in history :
			e.append([])
			
			chef = Users.query.filter_by(id_user=i.id_user).first()

			if i.line == "Eps":
				oldreff = Eps_reff.query.filter_by(id_eps_ref=i.old_ref_id).first()
				newreff = Eps_reff.query.filter_by(id_eps_ref=i.new_ref_id).first()
				oldid=oldreff.id_eps_ref
				newid=newreff.id_eps_ref
			elif i.line == "half shaft" :
				oldreff = Half_shift_ref.query.filter_by(id_hs_ref=i.old_ref_id).first()
				newreff = Half_shift_ref.query.filter_by(id_hs_ref=i.new_ref_id).first()
				oldid=oldreff.id_hs_ref
				newid=newreff.id_hs_ref	
			else :
				continue
			e[r].append(i.line)
			e[r].append(chef.name)
#			e[r].append(oldreff.axle_bar_num)
#			e[r].append(newreff.axle_bar_num)
			e[r].append(oldid)
			e[r].append(newid)
			e[r].append(i.date_changed)
			r+=1
	e.reverse()
	return render_template('logistic.html',history=e,currentusers=l,name=session["user_name"])

# Route /change_ref 'Change Reference'
@app.route("/change_ref",methods=["POST","GET"])
def change_ref():
	form_change = chose_ref()
	form =chose_ref()
	if session["user_line"] == 1 :
		line="EPS"
	else:
		line="Half Shaft"
	if form_change.validate_on_submit():
		id_chef = form_change.id.data
		form_change.id.data = ''
		user_idd = session["user_id"]
		usr = Current_reff.query.filter_by(id_user=user_idd).first()
		db.session.delete(usr)
		db.session.commit()
		if session["user_line"] == 1 :
			ref = Eps_reff.query.filter_by(id_eps_ref=id_chef).first()
		else : 
			ref = Half_shift_ref.query.filter_by(id_hs_ref=id_chef).first()
		if ref is None:	
			flash("Wrong Reference")
			return redirect(url_for('change_ref'))
		usrid=session["user_id"]
		cr= Current_reff(id_user=usrid , id_ref=id_chef)
		db.session.add(cr)
		db.session.commit() 
		old_ref = session["user_cuurent_ref"]
		new_ref = id_chef
		userline = session["user_line"]
		if userline == 2 :
			userline = 'half shaft'
		else :
			userline = 'Eps'
		change = Change_his(id_user=usrid ,line =userline,old_ref_id=old_ref,new_ref_id=new_ref)
		db.session.add(change)
		db.session.commit()
		session["user_cuurent_ref"]=new_ref
		return render_template("production.html",abadila =True,form=form,form_change=form_change,ref =new_ref,line=line,zone=session["user_zone"],name=session["user_name"])
	else:
		return render_template("production.html",abadila =True,form=form,form_change=form_change,line=line,zone=session["user_zone"],name=session["user_name"])

# Route /logout
@app.route("/logout",methods=["POST","GET"])
def logout ():
	if "user_id" in session:
		user_idd = session["user_id"]
		usser = session["user_name"]
		logistic_user = Logistic.query.filter_by(name = usser).first()
		
		if logistic_user is not None :
			
			session.pop("user_id",None )
			session.pop("user_name",None )
			session.pop("user_password",None )
			return redirect(url_for("login"))

		usr = Current_reff.query.filter_by(id_user=user_idd).first()
		db.session.delete(usr)
		db.session.commit()
		session.pop("user_id",None )
		session.pop("user_name",None )
		session.pop("user_password",None )
		session.pop("user_line",None )
		session.pop("user_zone",None )
		session.pop("user_cuurent_ref",None )
		return redirect(url_for("login"))
	else:	
		return 'login first'



if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)
