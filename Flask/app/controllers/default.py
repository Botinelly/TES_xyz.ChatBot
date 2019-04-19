import time
from flask import render_template, flash, url_for, redirect, Flask, send_file
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date
from app import app, db, lm
from io import BytesIO

from selenium import webdriver
from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
#@login_required
def index():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    drive = webdriver.Chrome(chrome_options=options)

    EMAIL ="rafds.snf@uea.edu.br"
    SENHA = "1515310023"

    NUM_PROTOCOLO = "201900006908"
    SENHA_PROTOCOLO = "d122af"

    URL_HORARIOS = "http://177.66.10.35/lyceump/aonline/horario.asp"
    URL_NOTAS = "http://177.66.10.35/lyceump/aonline/notas_freq.asp"
    URL_PROTOCOLO = "http://www1.uea.edu.br/modulo/login/protocolo.php"

    XPATH_HORARIOS = "//*[@id='ctnTabPagina2']/table/tbody/tr/td/table[2]"
    XPATH_NOTAS = "//*[@id='ctnTabPagina2']/table/tbody/tr/td/table"

    def uea_login():
        drive.get("http://www2.uea.edu.br/modulo/login/lyceum2.php")
        drive.find_element_by_id("email").send_keys(EMAIL)
        drive.find_element_by_id("senha").send_keys(SENHA)
        drive.find_element_by_class_name("btn").click()
        time.sleep(5)

    def uea_horario():
        drive.get(URL_HORARIOS)
        print(drive.current_url)

        xpath_horarios = drive.find_elements_by_xpath(XPATH_HORARIOS)[0]
        lista_de_horarios = xpath_horarios.text
        print(lista_de_horarios)

    def uea_notas():
        drive.get(URL_NOTAS)
        print(drive.current_url)

        xpath_notas = drive.find_elements_by_xpath(XPATH_NOTAS)[0]
        lista_de_notas = xpath_notas.text
        print(lista_de_notas)

    def uea_protocolo():
        drive.get(URL_PROTOCOLO)
        print(drive.current_url)

        drive.find_element_by_id("procId").send_keys(NUM_PROTOCOLO)
        drive.find_element_by_id("password").send_keys(SENHA_PROTOCOLO)
        drive.find_element_by_class_name("btn").click()
        time.sleep(5)

        info_proc = drive.find_element_by_class_name("panel")
        info = info_proc.text
        print(info)

    log = uea_login()
    hor = uea_horario()
    nota = uea_notas()
    prot = uea_protocolo()
    return render_template('index.html', log = log, hor = hor, nota = nota, prot = prot)

@app.route("/", methods=["POST", "GET"])
@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Login Inválido")

    return render_template('login.html', form = form)

@app.route("/register", methods=["POST", "GET"])
@login_required
def register():
    rf = RegisterForm()
    if rf.validate_on_submit():
        if rf.password.data == rf.password2.data:
            if rf.admin.data:
                user = User(rf.username.data, rf.password.data, 1)
                db.session.add(user)
                db.session.commit()
                flash('Registrado !')
                return redirect(url_for('index'))
            else:
                user = User(rf.username.data, rf.password.data, 0)
                db.session.add(user)
                db.session.commit()
                flash('Registrado !')
                return redirect(url_for('index'))
        else:
            flash('Senhas não condizem !')
    return render_template('register.html', rf = rf)

@app.route("/logout")
def logout():
    logout_user()
    flash("Deslogado")
    return redirect(url_for("login"))
