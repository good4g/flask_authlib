from flask import session, render_template, url_for, redirect
from main import oauth


# Домашняя страница, проверяется есть ли в сессии юзер
def homepage():
    user = session.get('user')
    return render_template('home.html', user=user)


# авторизует и перекидывает на страницу auth
def login():
    redirect_uri = url_for('main_bp.auth', _external=True)
    print(redirect_uri)
    return oauth.google.authorize_redirect(redirect_uri)


# меняет данные в сессии
def auth():
    token = oauth.google.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/')


# выход, удаляет юзера из сессии
def logout():
    session.pop('user', None)
    return redirect('/')