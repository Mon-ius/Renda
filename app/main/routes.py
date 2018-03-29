from flask import render_template,url_for,\
                redirect,flash,request,g,jsonify, current_app

from flask_babel import _, get_locale
from app.models import Post

from app.main.forms import PostForm

from app.main import bp



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])

def index():
    form = PostForm()
    return render_template(
        'main/index.html',
        title=_('Home'),
        res=1
        )


@bp.route('/explore', methods=['GET', 'POST'])
def explore():
    return render_template(
        'main/explore.html',
        title=_('Explore'),
        res=1
        )
