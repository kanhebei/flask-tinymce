"""
    Flask-TinyMce
    @Time    : 2020/2/1 11:29
    @Author  : wumao
    @Email   : kanhebei@dingtalk.com
"""
from flask import Blueprint, current_app, url_for, Markup


VERSION_TINYMCE = '5.1.1'


class _TinyMce(object):
    @staticmethod
    def config(selector='#body', **kwargs):
        plugins = kwargs.get('plugins', current_app.config['TINYMCE_PLUGINS'])
        tool_bar = kwargs.get('tool_bar', current_app.config['TINYMCE_TOOLBAR'])
        return Markup('''
<script type="text/javascript">
    tinymce.init({
            convert_urls: false,
            selector: "%s",
            height: 280,
            menubar: false,
            toolbar: "%s",
            plugins: "%s".split(",")
        });
</script>''' % (selector, ' '.join(tool_bar), ','.join(plugins)))

    @staticmethod
    def load(version=VERSION_TINYMCE):
        serve_local = current_app.config['TINYMCE_SERVE_LOCAL']
        js_filename = 'tinymce.min.js'
        if serve_local:
            js = '<script src="{}"></script>'.format(url_for('tinymce.static', filename=js_filename))
        else:
            js = '<script src="https://cdn.jsdelivr.net/npm/tinymce@{}/{}"></script>'.format(version, js_filename)

        return Markup(js)

    @staticmethod
    def create(class_='form-control', name='', value=''):
        return Markup('<textarea class="{0}" id="{1}" name="{1}">{2}</textarea>'.format(
            class_,
            name,
            value
        ))


class Tinymce(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        blueprint = Blueprint(
            'tinymce',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/tinymce' + app.static_url_path
        )
        app.register_blueprint(blueprint)
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['tinymce'] = _TinyMce()
        app.context_processor(self.context_processor)
        app.jinja_env.globals['tinymce'] = self
        # default settings
        app.config.setdefault('TINYMCE_SERVE_LOCAL', False)
        app.config.setdefault(
            'TINYMCE_TOOLBAR',
            [
                'format', 'undo', 'redo', 'searchreplace', 'bold', 'italic', 'underline',
                'alignleft', 'aligncenter', 'aligncenter', 'alignright', 'outdent',
                'indent', 'image', 'wordcount', 'preview', 'fullscreen'
            ]
        )
        app.config.setdefault(
            'TINYMCE_PLUGINS',
            ["preview", "fullscreen", "wordcount", "image", "searchreplace"]
        )

    @staticmethod
    def context_processor():
        return {'tinymce': current_app.extensions['tinymce']}

