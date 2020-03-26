from flask import Flask, templating

app = Flask(__name__)
@app.route('/')
def home():
    return "Theatron"

@app.route('/privacypolicy/')
def privacypolicy():
    return templating.render_template('privacy.html')


@app.route('/termsandconditions/')
def termsandc():
    return templating.render_template('tnc.html')


app.run()
