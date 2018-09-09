from flask import Flask

def regist_blueprint(app):
    @app.route('/')
    def hello_world():
        return 'Hello World!'

def create_app():
    app = Flask(__name__)
    regist_blueprint(app)
    return app


app = create_app()




if __name__ == '__main__':
    app.run()
