from flask import Flask, render_template, request, redirect, flash, session
from cs50 import SQL
from datetime import datetime
import pytz
IST = pytz.timezone('Asia/Kolkata')

app = Flask(__name__)
app.secret_key = "thesecretkey"

db = SQL("sqlite:///task.db")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        task = request.form.get("task")
        timestamp = datetime.now(IST).strftime("%Y-%m-%d (%H:%M:%S)")  # Current date and time in IST

        if not name and task:
            flash("Enter the Subject!")
            return redirect("/")

        elif not task and name:
            flash("Enter the task also!")
            return redirect("/")
        elif not task and not name:
            flash("Enter the Details!")
            return redirect("/")

        # Insert the task with the timestamp
        db.execute("INSERT INTO tasks (name, task, timestamp) VALUES (?, ?, ?)", name, task, timestamp)
        return redirect("/")

    else:
        tasks = db.execute("SELECT * FROM tasks")
        return render_template("index.html", tasks=tasks)
@app.route("/done", methods=["GET","POST"])
def done():
    if request.method == "POST":
        id = request.form.get("id")
        db.execute("delete from tasks where id=?", id )
        return redirect("/")

    else:
        return render_template("index.html")


@app.route("/amend", methods=["GET", "POST"])
def amend():
    if request.method == "POST":
        id = request.form.get("id")
    else:  # For GET request, retrieve the id from the query string
        id = request.args.get("id")

    if not id:
        flash("Invalid task ID!")
        return redirect("/")

    task = db.execute("SELECT * FROM tasks WHERE id = ?", id)
    if not task:
        flash("Task not found!")
        return redirect("/")

    return render_template("amend.html", task=task)



@app.route("/amendt", methods =["GET","POST"])
def amendt():
    if request.method == "POST":
        task_id = request.form.get('id')
        subject = request.form.get("subject")
        atask = request.form.get("atask")
        timestamp = datetime.now(IST).strftime("%Y-%m-%d (%H:%M:%S) ")

        if not subject and not atask:
            flash("Enter the Details!")
            return redirect(f"/amend?id={task_id}")

        elif not atask and subject:
            flash("Enter the task also")
            return redirect(f"/amend?id={task_id}")

        elif atask and not subject:
            flash("Enter the Subject!")
            return redirect(f"/amend?id={task_id}")

        db.execute("UPDATE tasks SET name = ?, task = ?, timestamp = ? WHERE id = ?", subject, atask, timestamp, task_id)
        return redirect("/")










