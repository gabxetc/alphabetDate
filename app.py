from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # Just referencing this file
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///test.db"  # 4 slashes is an absolute path, 3 is a relative path -> this is where the database is located
)
db = SQLAlchemy(app)  # initialising database

'''Table/database structure and intialising attributes of the database'''
class Dates(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id of the date
    content = db.Column(db.String(200), nullable=False)  # name of the date
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # when the date was created
    # completed = db.Column(db.Boolean, nullable=False)  # if the date has been gone on

    def __repr__(self) -> str:
        return "<Date: %r>" % self.id


"""Creates a new date"""
@app.route(
    "/", methods=["POST", "GET"]
)  # index route so we dont immediately get a 404 // Pass in the url string of my site (we've also added two methods the route can accept allowing us to not only get info but post info to our db)
def index():
    if request.method == "POST":
        date_content = request.form["content"]
        new_date = Dates(content=date_content)

        try:
            db.session.add(new_date)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your date"
    else:
        thedate = Dates.query.order_by(
            Dates.date_created
        ).all()  # looks at tall the database content in the order of date created and returns them
        return render_template("index.html", thedate=thedate)  # <- Name of the file


"""Deletes the selected date"""
@app.route("/delete/<int:id>")
def delete(id):
    date_to_delete = Dates.query.get_or_404(
        id
    )  # attemps to get the date by id and if it doesnt we'll get a 404

    try:
        db.session.delete(date_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting that date"


"""Updates the selected date"""
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    date_to_update = Dates.query.get_or_404(
        id
    )  # getting the task from the id and passing it in the url

    if request.method == "POST":
        date_to_update.content = request.form['content'] # setting the content of the date_to_update variable to new content submitted in the form

        try:
            db.session.commit() # we just commit because we're not adding anything, we're updating
            return redirect('/')
    
        except:
            return 'There was an issue updating your date information'
    else:
        return render_template("update.html", date_to_update=date_to_update)


if __name__ == "__main__":
    app.run(debug=True)
