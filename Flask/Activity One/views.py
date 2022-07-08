from flask import Flask, render_template, Blueprint, redirect, url_for


my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/Page1')
def Page1():
    return render_template("Page1.html")

@my_view.route('/Page2')
def Page2():
    return render_template("Page2.html")

@my_view.route('/Page3')
def Page3():
    return render_template("Page3.html")

@my_view.route('/Admin')
def Admin():
    return render_template("Admin.html")

# @my_view.route('/404')
# def 404()
#     return render_template("404.html")
#add as many reidrects as you want, think google ad words searches returning 404 errors on log
@my_view.route('/Home')
@my_view.route('/js')
@my_view.route('/javascript')
def about_redirect():
    return redirect(url_for("my_view.index"))

