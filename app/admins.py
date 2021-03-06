from flask_admin.contrib.sqla import ModelView
from app import db, admin, utils
from app.models import Event
from flask.ext.login import current_user
from flask import redirect, url_for, request


class EventAdmin(ModelView):
    column_display_pk = True
    form_widget_args = {
        'slug':{
            'disabled':True
        }
    }
    def is_accessible(self):
        return current_user.is_authenticated()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))

    def on_model_change(self, form, instance, is_created):
        instance.slug = utils.slugify(form.title.data)
        super(EventAdmin, self).on_model_change(form, instance, is_created)

admin.add_view(EventAdmin(Event, db.session))
