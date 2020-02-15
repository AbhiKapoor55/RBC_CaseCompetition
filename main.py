from flask import Flask, url_for, render_template, request, Response, redirect, jsonify
from flask_static_compress import FlaskStaticCompress

app = Flask(__name__)
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
app.config['COMPRESSOR_OUTPUT_DIR'] = 'build'
app.static_folder = 'static'
compress = FlaskStaticCompress(app)



@app.route('/', methods=['GET'])
def home():
    """Landing page."""
    return redirect(url_for('static', filename='index.html'))

@app.route('/launchDivi', methods=['GET'])
def launchDivi():
    return redirect(url_for('static', filename='chatbot.html'))


if __name__ == "__main__":
    app.run()