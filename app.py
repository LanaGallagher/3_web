from flask import Flask, render_template, request
from pwdGen import pwdGenerator
import db

DB_PATH = "/home/LanaGallagher13/3_web/database/site.db" #"database/site.db"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/page2", methods=["GET", "POST"])
def page_2():
    result = ""
    if request.method == "POST":
        password = request.form.get("pwd")
        salt = request.form.get("salt")
        num = request.form.get("num")

        if password != None and salt != "" and num != "":
            result = pwdGenerator(password, salt, num)
            if num.isnumeric():
                db.write_db(DB_PATH, [(password, salt, int(num), result)])
            else:
                db.write_db(DB_PATH, [(password, salt, len(result), result)])
        
        else:
            result = ""

    return render_template("page2.html", data=result)

@app.route("/page3")
def page_3(): 
    return render_template("page3.html", data = db.read_db(DB_PATH))

@app.route("/test")
def page_4():
    val_1 = request.args.get("par_1")
    val_2 = request.args.get("par_2")
    return render_template("test.html", v1=val_1, p2=val_2)

if __name__ == "__main__":
    db.create_db(DB_PATH)
    app.run() #debug=True)