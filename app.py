from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cape_town")
def cape_town():
    return render_template("cape_town.html")

@app.route("/durban")
def durban():
    return "PAGE UNDER CONSTRUCTION"

@app.route("/johannesburg")
def johannesburg():
    return "PAGE UNDER CONSTRUCTION"

@app.route("/cape_town_accommodation")
def cape_town_accommodation():
    return render_template("cape_town_accommodation.html")

@app.route("/protel_hotel")
def protea_hotel():
    return render_template("protel_hotel.html")

@app.route("/margot_hotel")
def margot_hotel():
    return render_template("margot_hotel.html")

@app.route("/cape_town_activities")
def cape_town_activities():
    return render_template("cape_town_activities.html")

@app.route("/atlantis_dunes")
def atlantis_dunes():
    return render_template("atlantis_dunes.html")

@app.route("/book_standard")
def book_standard():
    return render_template("book_standard.html")

@app.route("/book/atlantis_dunes/standard")
def book_atlantis_standard():
    return render_template("book_atlantis_standard.html")

@app.route("/book/atlantis_dunes/luxury")
def book_atlantis_luxury():
    return render_template("book_atlantis_luxury.html")




@app.route("/cape_town_restaurants")
def cape_town_restaurants():
    return render_template("cape_town_restaurants.html")



if __name__ == "__main__":
    app.run(debug=True, port=5051)