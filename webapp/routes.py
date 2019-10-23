from flask import render_template, url_for, flash, redirect
from webapp import app, db, bcrypt
from webapp.forms import RegistrationForm, LoginForm, PairForm, SingleForm
from webapp.models import User, Pair
from flask_login import login_user, current_user
from sqlalchemy import func, desc


@app.route('/', methods=['GET', 'POST']) #'/' tells us that it's the index of a page | access via  http://127.0.0.1:5000/
def home():
    form = PairForm()
    if form.validate_on_submit():
        #user = current_user.id or something
        pair = Pair(firstname=form.firstname.data, secondname=form.secondname.data, firstartist=form.firstartist.data, secondartist=form.secondartist.data, comment=form.comment.data, firstgenre=form.firstgenre.data, secondgenre=form.secondgenre.data, guestname=form.guestname.data) ## TODO: add user_id info from current user ID
        db.session.add(pair)
        db.session.commit() # adds user to database
        flash(f'Success! Your transition was added. {form.firstname.data} and {form.secondname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('index.html', title="Save DJ Transition", form=form)

@app.route('/singlesong', methods=['GET', 'POST']) #'/' tells us that it's the index of a page | access via  http://127.0.0.1:5000/
def singlesong():
    form = SingleForm()
    if form.validate_on_submit():
        #user = current_user.id or something
        pair = Pair(firstname=form.firstname.data, secondname=None, firstartist=form.firstartist.data, secondartist=None, comment=form.comment.data, guestname=form.guestname.data) ## TODO: add user_id info from current user ID # create pair instance with input from form
        db.session.add(pair)
        db.session.commit() # adds user to database
        flash(f'Success! Your single song was added. {form.firstname.data} - {form.firstartist.data}!', 'success')
        return redirect(url_for('singlesong'))
    return render_template('singlesong.html', title="Single Song", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: ## DEBUG: doens't work # TODO: if logged in redirect to home
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # hashes entered password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # create user instance with input from form
        db.session.add(user)
        db.session.commit() # adds user to database
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() #database will be filtered with entered email
        if user and bcrypt.check_password_hash(user.password, form.password.data): #check password and email
            login_user(user, remember=form.remember.data) #login_user() logs user in
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger') #danger makes return red #TODO: get success and danger colored frames working
    return render_template('login.html', title='Login', form=form)

@app.route('/transitions', methods=['GET', 'POST'])
def transitions():
    pairs = Pair.query.order_by(desc(Pair.date_posted)).all() #order by date_posted - show newest first
    return render_template('transitions.html', title='Transitions Database', pairs=pairs)

@app.route('/searchguest/<guestname>', methods=['GET', 'POST'])
def searchguest(guestname=None):
    #filter by guestname and order by date (show neweste first)
    posts = Pair.query.filter(func.lower(Pair.guestname) == func.lower(guestname)).order_by(desc(Pair.date_posted)).all()
    return render_template('searchguest.html', guestname=guestname, title="Search", posts=posts)

#DEBUG Routes
@app.route('/hello') # access via  http://127.0.0.1:5000/hello/anything
def hellos():
    return render_template('hello.html')

@app.route('/hello/<name>') # access via  http://127.0.0.1:5000/hello/*anything*
def helloTemplate(name=None):
    return render_template('hello.html', name=name, title="Debug Route")
