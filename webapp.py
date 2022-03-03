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

    cardict = {
     "C4": {"price":15000, "img":"c4.jpg"},
     "B2": {"price":8000, "img":"b2.jpg"},
     "Quattro": {"price":58000, "img":"quattro.jpg"},
     "D2": {"price":13000, "img":"d2.jpg"},
     "B7": {"price":25000, "img":"b7.jpg"},
     "R8": {"price":135000, "img":"r8.jpg"},
     "D4": {"price":36000, "img":"d4.jpg"},
     "TT": {"price":38000, "img":"tt.jpg"},
     "B9": {"price":28000, "img":"b9.jpg"},
     "Q8": {"price":115000, "img":"q8.jpg"},
     "02": {"price":38000, "img":"2002.jpg"},
     "e30": {"price":18000, "img":"e30.jpg"},
     "e31": {"price":30000, "img":"e31.jpg"},
     "e36": {"price":14000, "img":"e36.jpg"},
     "e39": {"price":13000, "img":"e39.jpg"},
     "e46": {"price":8000, "img":"e46.jpg"},
     "e89": {"price":25000, "img":"e89.jpg"},
     "f30": {"price":32000, "img":"f30.jpg"},
     "g11": {"price":62000, "img":"g11.jpg"},
     "g22": {"price":45000, "img":"g22.jpg"},
     "W123": {"price":13000, "img":"w123.jpg"},
     "W126": {"price":18000, "img":"w126.jpg"},
     "W201": {"price":5000, "img":"w201.jpg"},
     "R129": {"price":19000, "img":"r129.jpg"},
     "C208": {"price":28000, "img":"c208.jpg"},
     "W463": {"price":133000, "img":"w463.jpg"},
     "R230": {"price":20000, "img":"r230.jpg"},
     "C199": {"price":264000, "img":"c199.jpg"},
     "C190": {"price":92000, "img":"c190.jpg"},
     "W116": {"price":200000, "img":"w116.jpg"},
    }
    return render_template('moneypage.html')

if __name__=="__main__":
    app.run(debug=False)
