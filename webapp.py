from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/displaypage")
def render_displaypage():

    brand = request.args['brands']
    if brand == 'bmw':
        dpage = 'bpage.html'
    elif brand == 'benz':
        dpage = 'mpage.html'
    elif brand == 'audi':
        dpage = 'apage.html'
    return render_template(dpage)

@app.route("/moneypage")
def render_moneypage():
    return render_template('moneypage.html')

if __name__=="__main__":
    app.run(debug=False)
