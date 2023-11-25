from flask import Flask,render_template,session,redirect
app=Flask(__name__)
app.secret_key="hello world!"

@app.route('/')
def index():
    if "count" not in session:
        session["count"]= 0
    else:
        session["count"] += 1

    return render_template("index.html")


@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/by_two')
def by_two():
    session["count"] += 1
    
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)

