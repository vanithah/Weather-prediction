from flask import Flask, render_template, redirect, url_for, request
import wed

app = Flask(__name__, template_folder='template')


@app.route("/", methods=["POST", "GET"])
def form():
    return(render_template("form.html"))


@app.route("/success", methods=["GET", "POST"])
def success():
    if(request.method == "POST"):
        city = request.form["nm"]
        app1 = wed.wea(str(city))
        data = app1.find_data()
        return render_template("success.html", data=data)
        
if __name__ == "__main__":
    app.run(debug=True)

