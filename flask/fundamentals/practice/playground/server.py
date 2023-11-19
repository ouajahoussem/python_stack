from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", num = 3, color= "lightblue")

@app.route ('/play/<int:num>')
def level_2(num):
    return render_template("index.html",num=num, color="lightblue")

@app.route ('/play/<int:num>/<string:color>')
def level_3(num,color):
    return render_template("index.html",num=num, color=color)







if __name__ == "__main__":
    app.run(debug=True)