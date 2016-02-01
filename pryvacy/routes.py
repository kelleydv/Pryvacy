from . import app
from . import controllers
from flask import render_template, redirect, url_for, flash
from flask import session, request

import markdown2
import os


@app.route('/')
def index():
    return render_template('home.html', session=session)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register the user."""
    if session.get('user'):
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        error = controllers.signup(
            request.form['username'],
            request.form['password'],
            request.form['password2']
        )
        if not error:
            flash('You were successfully registered and can login now')
            return redirect(url_for('home.login'))
    return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if session.get('user'):
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        user = controllers.authenticate_user(request.form['username'], request.form['password'])
        if user:
            flash('Welcome back %s' % user['username'])
            session['user'] = user
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error, session=session)


@app.route('/logout')
def logout(msg='You were logged out'):
    """Logs the user out."""
    flash(msg)
    session.clear()
    return redirect(url_for('index'))


@app.route('/page/<name>')
def page(name=None):
    path = os.path.join(os.getcwd(), 'pryvacy', 'content', name + '.md')

    if not os.path.isfile(path):
        # TODO Create a 404 page
        flash('Page not found')
        return redirect(url_for('index'))

    with open(path) as f:
        text = f.read()
        content = markdown2.markdown(text)
        title = text.split('\n').pop(0)[2:].strip()

    return render_template('pages/page.html', title=title, content=content)


@app.route('/feed')
def feed():
    ip = request.remote_addr
    agent = request.user_agent
    print(ip)
    print(agent.browser)
    return render_template('feed.html', session=session)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        return render_template('profile.html', session=session)
