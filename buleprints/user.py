import email
from email import message
from async_timeout import timeout
from flask import Blueprint,render_template,request
from flask_mail import Message
from exts import mail,cache
import random
from flask import current_app


bp = Blueprint('user',__name__,url_prefix='/user')

@bp.route('/register')
def register():
    return render_template('front/register.html')

@bp.route('/mail/captcha')
def mail_captcha():
    email = request.args.get('mail')
    digits = ['0','1','2','3','4','5','6','7','8','9']
    captcha = ''.join(random.sample(digits,4))
    subject = '【知了Python论坛】注册验证码'
    body = f'【知了Python论坛】您的注册验证码是：{captcha}，请勿告诉别人！！'
    current_app.celery.send_task('send_mail',(email,subject,body))
    cache.set(email,captcha,timeout=100)
    return 'success'