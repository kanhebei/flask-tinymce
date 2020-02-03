# @Time    : 2020/2/1 11:52
# @Author  : wumao
# @Email   : kanhebei@dingtalk.com

from wtforms import TextAreaField
from wtforms.widgets import TextArea


class TinyMce(TextArea):
    def __call__(self, field, **kwargs):
        # c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        # kwargs['class'] = u'%s %s' % ('tinymce', c)
        return super(TinyMce, self).__call__(field, **kwargs)


class TinyMceField(TextAreaField):
    widget = TinyMce()
