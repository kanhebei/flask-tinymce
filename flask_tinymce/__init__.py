from flask import Blueprint, current_app, url_for, Markup
import json

__VERSION__ = '1.0.0'
__AUTHOR__ = 'wumao'
__EMAIL__ = 'kanhebei@dingtalk.com'

class TinyMCEHelper:
    def init(self, selector, **kwargs):
        kwargs['selector'] = selector
                       
        if all(
            (
                'language' not in kwargs,
                'language' not in current_app.config['TINYMCE_CONFIG'],
                current_app.config['TINYMCE_LANGUAGE']
            )
        ):
            kwargs['language'] = current_app.config['TINYMCE_LANGUAGE']

        for k, v in current_app.config['TINYMCE_CONFIG'].items():
            if k not in kwargs:
                kwargs[k] = v


        js = '<script type="text/javascript">tinymce.init(%s)</script>'
        return Markup(js % json.dumps(kwargs))

    def load_js(self, src=None):
        if src is not None:
            return Markup('<script src="%s"></script>' % src)

        if current_app.config['TINYMCE_SERVE_LOCAL'] is True:
            return Markup('<script src="%s"></script>' % url_for('tinymce.static', filename='tinymce.min.js'))

        return Markup('<script src="{src}" referrerpolicy="origin"></script>'.format(
            'https://cdn.tiny.cloud/1/%s/tinymce/5/tinymce.min.js' % current_app.config['TINYMCE_API_TOKEN']
        ))


class TinyMCE:
    def __init__(self, app=None, helper=TinyMCEHelper):
        self.app = app

        self.helper = helper() 

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        blueprint = Blueprint(
            'tinymce',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/tinymce'
        )
        app.register_blueprint(blueprint)
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['tinymce'] = self.helper
        app.context_processor(lambda : {'tinymce': self.helper})
        
        # 使用扩展自带的资源
        app.config.setdefault('TINYMCE_SERVE_LOCAL', True)
        # 非本地资源 填写tinymce 的API_TOKEN
        app.config.setdefault('TINYMCE_API_TOKEN', 'no-api-key')
        app.config.setdefault('TINYMCE_LANGUAGE', 'zh_CN')
        app.config.setdefault('TINYMCE_CONFIG', {})
