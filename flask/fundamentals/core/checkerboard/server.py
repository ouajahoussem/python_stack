from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def task_1():
    return render_template("index.html",row=8 ,col=8, color1='red', color2='black')

@app.route('/<int:x>')
def task_2(x):
    return render_template("index.html",row=x ,col=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def task_3(x,y):
    return render_template("index.html",row=x ,col=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def task_4(x,y,color1,color2):
    return render_template("index.html",row=x ,col=y, color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True)