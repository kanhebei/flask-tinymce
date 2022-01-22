
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_tinymce import TinyMCE
from flask import Flask, render_template


app = Flask(__name__)

TinyMCE(app) 
"""
or

tinymce = Tinymce()
tinymce.init_app(app)
"""

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
