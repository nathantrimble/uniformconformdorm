from flask import Flask, url_for, render_template, request, url_for

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)



@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/displaypage", methods =['GET','POST'])
def render_displaypage():

    brand = request.form['brands']
    if brand == 'bmw':
        dpage = 'bpage.html'
        info = "Bayerische Motoren Werke AG, commonly referred to as BMW, is a German multinational corporate manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany. The corporation was founded in 1916 as a manufacturer of aircraft engines, which it produced from 1917 until 1918 and again from 1933 to 1945. Automobiles are marketed under the brands BMW, Mini and Rolls-Royce, and motorcycles are marketed under the brand BMW Motorrad. In 2017, BMW was the world's fourteenth-largest producer of motor vehicles, with 2,279,503 vehicles produced. The company has significant motorsport history, especially in touring cars, Formula 1, sports cars and the Isle of Man TT. BMW is headquartered in Munich and produces motor vehicles in Germany, Brazil, China, India, Mexico, the Netherlands, South Africa, the United Kingdom, and the United States."
    elif brand == 'benz':
        dpage = 'mpage.html'
        info = 'Mercedes-Benz, commonly referred to as just Mercedes, is a German luxury automotive marque. Both Mercedes-Benz and Mercedes-Benz AG (a Mercedes-Benz Group subsidiary established in 2019) are headquartered in Stuttgart, Baden-Württemberg, Germany. Mercedes-Benz produces consumer luxury vehicles and commercial vehicles.[note 2] Its first Mercedes-Benz-badged vehicles were produced in 1926. In 2018, Mercedes-Benz was the largest seller of premium vehicles in the world, having sold 2.31 million passenger cars.[8]The companys origins lie in Daimler-Motoren-Gesellschafts 1901 Mercedes and Karl Benzs 1886 Benz Patent-Motorwagen, which is widely regarded as the first internal combustion engine in a self-propelled automobile. The slogan for the brand is "the best or nothing".'
    elif brand == 'audi':
        dpage = 'apage.html'
        info = 'Audi AG (commonly referred to as Audi) is a German automotive manufacturer of luxury vehicles headquartered in Ingolstadt, Bavaria, Germany. As a subsidiary of its parent company, the Volkswagen Group, Audi produces vehicles in nine production facilities worldwide.The origins of the company are complex, going back to the early 20th century and the initial enterprises (Horch and the Audiwerke) founded by engineer August Horch; and two other manufacturers (DKW and Wanderer), leading to the foundation of Auto Union in 1932. The modern Audi era began in the 1960s, when Auto Union was acquired by Volkswagen from Daimler-Benz. After relaunching the Audi brand with the 1965 introduction of the Audi F103 series, Volkswagen merged Auto Union with NSU Motorenwerke in 1969, thus creating the present-day form of the company.The company name is based on the Latin translation of the surname of the founder, August Horch. Horch, meaning "listen" in German, becomes audi in Latin. The four rings of the Audi logo each represent one of four car companies that banded together to create Audis predecessor company, Auto Union. Audis slogan is Vorsprung durch Technik, meaning "Being Ahead through Technology". Audi, along with fellow German marques BMW and Mercedes-Benz, is among the best-selling luxury automobile brands in the world.'
    return render_template(dpage, inf = info)

@app.route("/moneypage", methods=['GET','POST'])
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
    dbloon = (pric / 378)
    return render_template('moneypage.html', cheese = pric, broto = pic, nam = cname, db = dbloon)

if __name__=="__main__":
    app.run(debug=False)
