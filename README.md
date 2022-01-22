# Flask-TinyMce
[Flask]https://flask.palletsprojects.com/en/2.0.x/ 整合 [TinyMCE](https://www.tiny.cloud).的富文本编辑器扩展


## 如何开始：

from flask_tinymce import TinyMce

app = Flask(__name__)

TinyMCE(app)  
or  
mce = TinyMCE()
mce.init_app(app)

模板中如何使用：
    <textarea id="content" name="content"></textarea>
    1, 加载js
    {{ tinymce.load_js() }}
    2, 实例化tinymce
    {{ tinymce.init('#content') }}

自定义编辑器功能 
    {{ tinymce.init('#content', toolbar="undo redo | link image | code", menubar=False, height=300 )}}

深度定制tinymce：
    参考tinymce 官方文档
    使用js代码替换 {{ tinymce.init() }} 如下述
    <script>
        tinymce.init({
            ...
        })
    </script>