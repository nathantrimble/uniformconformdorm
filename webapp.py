from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

cardict = {
 "C4": {"price":15000, "img":"c4.jpg"},
 "B2": {"price":8000, "img":"c4.jpg"},
 "Quattro": {"price":58000, "img":"c4.jpg"},
 "D2": {"price":, "img":"c4.jpg"},
 "B7": {"price":, "img":"c4.jpg"},
 "R8": {"price":, "img":"c4.jpg"},
 "D4": {"price":, "img":"c4.jpg"},
 "TT": {"price":, "img":"c4.jpg"},
 "B9": {"price":, "img":"c4.jpg"},
 "Q8": {"price":, "img":""},
 "02": {"price":, "img":""},
 "e30": {"price":, "img":""},
 "e31": {"price":, "img":""},
 "e36": {"price":, "img":""},
 "e39": {"price":, "img":""},
 "e46": {"price":, "img":""},
 "e89": {"price":, "img":""},
 "f30": {"price":, "img":""},
 "g11": {"price":, "img":""},
 "g22": {"price":, "img":""},
 "W123": {"price":, "img":""},
 "W126": {"price":, "img":""},
 "W201": {"price":, "img":""},
 "R129": {"price":, "img":""},
 "C208": {"price":, "img":""},
 "W463": {"price":, "img":""},
 "R230": {"price":, "img":""},
 "C199": {"price":, "img":""},
 "C190": {"price":, "img":""},
 "W116": {"price":, "img":""},




}



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
