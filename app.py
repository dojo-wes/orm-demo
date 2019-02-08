import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def index():
    users = User.query.all()
    print(users)
    return render_template('index.html', data=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    user = User(name=request.form['name'])
    db.session.add(user)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
