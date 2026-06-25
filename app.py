from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{db_user}:{db_password}@db:5432/{db_name}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        note_text = request.form["content"]

        if note_text:
            note = Note(content=note_text)
            db.session.add(note)
            db.session.commit()

        return redirect("/")

    notes = Note.query.all()

    return render_template(
        "index.html",
        notes=notes
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
