from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, url_for, request
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, TanksForm
from application import app, db
from application.models import Users, Tanks

##############home #####################################################


@app.route('/')
@app.route('/home')
def home():
    postData = Tanks.query.all()
    return render_template('home.html', title='Home', tanks=postData)

#### Register User #########


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():

        user = Users(first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     email=form.email.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

##### login #####


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        login_user(user)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('register'))
    return render_template('login.html', title='Login', form=form)

### update account ####


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


#### create tests ####

@app.route('/tanks', methods=['GET', 'POST'])
@login_required
def tanks():
    form = TanksForm()
    if form.validate_on_submit():
        tanks = Tanks.query.filter_by(name=form.name.data).first()
        tankdata = Tanks(name=form.name.data,
                         description=form.description.data,
                         ammonia=form.ammonia.data,
                         nitrate=form.nitrate.data,
                         nitrite=form.nitrite.data,
                         author=current_user)

        db.session.add(tankdata)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('tanks.html', title='Tanks', form=form)

####### logout #############


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

############## delete ####################


@app.route('/account/delete', methods=['GET', 'POST'])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    count = Tanks.query.filter_by(user_id=user).count()
    for i in range(count):
        tank = Tanks.query.filter_by(user_id=user).first()
        db.session.delete(tank)
        db.session.commit()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))
