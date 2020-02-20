from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from werkzeug.exceptions import HTTPException
from flask_login import login_required, current_user
from app.models import Users, Projetos
from app import db
import json


main = Blueprint('main', __name__)
data = json.load(open('sites.json'))

@main.route('/')
def index():
    return render_template('index.html', data=len(data['sites']))


@main.route('/painel')
def painel():
    projetos = Projetos.query.all()
    return render_template('painel.html', projetos=projetos)


@main.route('/sites')
def sites():
    return jsonify(data['sites'])


@main.route('/import')
def import_sites():
    for site in data['sites']:
        exist = Projetos.query.filter_by(url=site).first()
        if not exist:
            projeto = Projetos(url=site)
            db.session.add(projeto)
            db.session.commit()
    return 'ok'


@main.route('/projetos')
def projetos():
    projetos = Projetos.query.all()
    all_projetos = []
    for projeto in projetos:
        all_projetos.append(f'{projeto.protocol}{projeto.url}')
    return jsonify(all_projetos)


@main.route('/projetos/new', methods=['GET', 'POST'])
def new_projeto():
    if request.method == 'POST':
        protocol = request.form['protocol']
        url = request.form['url']
        projeto = Projetos(protocol=protocol, url=url)
        db.session.add(projeto)
        db.session.commit()
        return redirect(url_for('main.painel'))
    return 'erro'


@main.route("/projetos/<int:projeto_id>/delete", methods=['GET'])
def delete_projeto(projeto_id):
    projeto = Projetos.query.get_or_404(projeto_id)
    db.session.delete(projeto)
    db.session.commit()
    return redirect(url_for('main.painel'))


@main.route("/projetos/<int:projeto_id>/edit", methods=['GET', 'POST'])
def edit_projeto(projeto_id):
    projeto = Projetos.query.get_or_404(projeto_id)
    projeto.protocol = request.form['protocol']
    projeto.url = request.form['url']
    db.session.commit()
    return redirect(url_for('main.painel'))


@main.route('/profile/<string:username>')
# @login_required
def get_profile(username):
    user = Users.query.filter_by(username=username).first()
    if not user:
        return render_template('profile.html'), 404
    return render_template('profile.html', user=user)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@main.errorhandler(HTTPException)
def handle_exception(e):
    e.get_response()

    code = e.code
    name = e.name
    desc = e.description

    return render_template('error.html',
    error = {
    	'code': code,
    	'name': name,
    	'description': desc
    })
