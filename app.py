from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # Just referencing this file
app.config["SQLALCHEMY_DATABASE_URI"] = (
    'sqlite:///test.db'  # 4 slashes is an absolute path, 3 is a relative path -> this is where the database is located
)
db = SQLAlchemy(app)  # initialising database


class Dates(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id of the date
    content = db.Column(db.String(200), nullable=False)  # name of the date
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # when the date was created
    # completed = db.Column(db.Boolean, nullable=False)  # if the date has been gone on

    def __repr__(self) -> str:
        return "<Date: %r>" % self.id


@app.route(
    "/"
)  # index route so we dont immediately get a 404 // Pass in the url string of my site
def index():
    return render_template("index.html")  # <- Name of the file


if __name__ == "__main__":
    app.run(debug=True)
