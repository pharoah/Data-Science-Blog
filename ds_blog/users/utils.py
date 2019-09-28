import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from ds_blog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pic', picture_fn)
    output_size = (125, 125)
    profile_img = Image.open(form_picture)
    profile_img.thumbnail(output_size)

    profile_img.save(picture_path)
    return picture_fn


def send_password_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender = 'no-reply@ds-blog.com', recipients = [user.email])
    msg.body = f'''Hi user.username, \n You have submitted a request to reset your password.
                  Please follow link to reset your password. \n
                  {url_for('users.reset_token', token = token, _external = True)} \n
                  If you did not make this request, please ignore this email and no changes will be made your account.\n

                  Thank you.
                  '''
    mail.send(msg)
