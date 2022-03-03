from flask import Flask, url_for, render_template, request, url_for

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
     "C4": {"price":15000, "img":"c4.jpg", "name":"100 C4 (1989-1993)"},
     "B2": {"price":8000, "img":"b2.jpg", "name":"80 B2 (1979-1986)"},
     "Quattro": {"price":58000, "img":"quattro.jpg", "name":"B2 Quattro (1980-1991)"},
     "D2": {"price":13000, "img":"d2.jpg", "name":"A8 D2 (1994-2002)"},
     "B7": {"price":25000, "img":"b7.jpg", "name":"A4 B7 (2004-2009)"},
     "R8": {"price":135000, "img":"r8.jpg", "name":"R8 42 (2006-2015)"},
     "D4": {"price":36000, "img":"d4.jpg", "name":"A8 D4 (2010-2017)"},
     "TT": {"price":38000, "img":"tt.jpg", "name":"TT 8S (2014-2022)"},
     "B9": {"price":28000, "img":"b9.jpg", "name":"A4 B9 (2016-2022)"},
     "Q8": {"price":115000, "img":"q8.jpg", "name":"Q8 (2019-2022)"},
     "02": {"price":38000, "img":"2002.jpg", "name":"2002 (1966-1977)"},
     "e30": {"price":18000, "img":"e30.jpg", "name":"E30 3-Series (1982-1994)"},
     "e31": {"price":30000, "img":"e31.jpg", "name":"E31 8-Series (1989-1999)"},
     "e36": {"price":14000, "img":"e36.jpg", "name":"E36 3-Series (1990-2000)"},
     "e39": {"price":13000, "img":"e39.jpg", "name":"E39 5-Series (1995-2003)"},
     "e46": {"price":8000, "img":"e46.jpg", "name":"E46 3-Series (1998-2006)"},
     "e89": {"price":25000, "img":"e89.jpg", "name":"E89 Z-4 Roadster (2009-2016)"},
     "f30": {"price":32000, "img":"f30.jpg", "name":"F30 3-Series (2011-2020)"},
     "g11": {"price":62000, "img":"g11.jpg", "name":"G11 7-Series (2015-2022)"},
     "g22": {"price":45000, "img":"g22.jpg", "name":"G22 4-Series (2020-2022)"},
     "W123": {"price":13000, "img":"w123.jpg", "name":"E-Class (1976-1986)"},
     "W126": {"price":18000, "img":"w126.jpg", "name":"S-Class (1979-1991)"},
     "W201": {"price":5000, "img":"w201.jpg", "name":"C-Class (1982-1993)"},
     "R129": {"price":19000, "img":"r129.jpg", "name":"SL-Class (1989-2002)"},
     "C208": {"price":28000, "img":"c208.jpg", "name":"CLK-Class (1997-2003)"},
     "W463": {"price":133000, "img":"w463.jpg", "name":"G-Wagon (1990-2018)"},
     "R230": {"price":20000, "img":"r230.jpg", "name":"SL-Class (2001-2011)"},
     "C199": {"price":264000, "img":"c199.jpg", "name":"SLR-Mclaren (2003-2010)"},
     "C190": {"price":92000, "img":"c190.jpg", "name":"AMG-GT (2015-2022)"},
     "W116": {"price":200000, "img":"w116.jpg", "name":"Maybach (2015-2022)"},
    }

    carmod = request.args['models']

    if  carmod in cardict:
        pric = cardict[carmod]['price']
        pic = cardict[carmod]['img']
        cname = cardict[carmod]['name']
    return render_template('moneypage.html', cheese = pric, broto = pic, nam = cname)

if __name__=="__main__":
    app.run(debug=False)
