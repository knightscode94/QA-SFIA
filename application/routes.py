from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, url_for, request
from application.forms import TestsForm, RegistrationForm, LoginForm, UpdateAccountForm, RegistrationTankForm
from application import app, db
from application.models import Users, Tanks, Tests

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
        return redirect(url_for('post'))
    return render_template('register.html', title='Register', form=form)

##### login #####

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        else:
            return redirect(url_for('home'))
    return render_template('log_in.html', title='Login', form=form)

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


#### create tank ####

@app.route('/tanks', methods=['GET', 'POST'])
@login_required
def registertank():
    form = RegistrationTankForm()
    if form.validate_on_submit():
        
        tanks = Tanks(name=form.name.data,
                description=form.description.data)
    
        db.session.add(tanks)
        db.session.commit()
        return redirect(url_for('tests'))
    return render_template('tanks.html', title='Tanks', form=form)

#### tests #####

@app.route('/tests', methods=['GET', 'POST'])
@login_required
def tests():
    form = TestsForm()
    if form.validate_on_submit():
        postData = Tests(
            title = form.title.data,
            content = form.content.data,
            author = current_user)

        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('test.html', title='Tests', form=form)

####### logout #############

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))