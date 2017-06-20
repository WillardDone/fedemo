from flask import Flask, render_template

class DevelopmentConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    CSRF_ENABLED = False

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/')
def game():
    return render_template('/game/game_index.html')


@app.route('/game/detail')
def game_detail():
    return render_template('/game/game_detail.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
