import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for

from helpers import usd

CONTROL_VARIABLE = 1.25
PRICE_PER_HOUR = 2.5

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///fashion-budget.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    """Show budget form"""
    # Get data from db to the form
    telas = db.execute("SELECT tela FROM telas")
    prendas = db.execute("SELECT prenda FROM prendas")
    acabadosAll = db.execute("SELECT acabado FROM acabados")

    if request.method == "POST":
        try:
            # Initialize error to false
            global error

            # Get all the data
            try:
                prenda = request.form.get("prenda")
                tela = request.form.get("tela")
                genero = request.form.get("genero")
                tallaGrande = request.form.get("talla-grande")
                cantidad = int(request.form.get("cantidad"))
                acabados = request.form.getlist("acabados[]")
            except ValueError:
                error = "Has ingresado valores inválidos"

            # Check if gender is valid
            if genero not in ["mujer", "hombre", "niño"]:
                error = "Has ingresado un género inválido"

            # Check if input prenda, tela, acabados exists in db
            rowsPrenda = db.execute(
                "SELECT dificultad FROM prendas WHERE prenda = ?", prenda
            )
            rowsTela = db.execute("SELECT dificultad FROM telas WHERE tela = ?", tela)

            if len(rowsPrenda) == 1 and len(rowsTela) == 1:
                difPrenda = rowsPrenda[0]["dificultad"]
                difTela = rowsTela[0]["dificultad"]

                # Calculate extra time depending on details
                extra = 0
                for acabado in acabados:
                    rowsAcabados = db.execute(
                        "SELECT tiempo_extra FROM acabados WHERE acabado = ?", acabado
                    )
                    if len(rowsAcabados) == 1:
                        extra += rowsAcabados[0]["tiempo_extra"]
                    elif acabado != "":
                        error = "Has ingresado un acabado inválido"

                # Calculate difficult coeficient
                difCoeficient = difPrenda + difTela + extra

            else:
                error = "Has ingresado valores inválidos"

            # Pay extra money if big size or gender is male
            if tallaGrande:
                difCoeficient += 1
            if genero == "hombre":
                difCoeficient += 1

            # Formula -> (difCoeficient + extra) x Control Variable x Price per hour x Quantity
            total = difCoeficient * CONTROL_VARIABLE * PRICE_PER_HOUR * cantidad

            # If total is calculated then send it to be shown
            app.logger.debug(acabados)
            return render_template(
                "calculator.html",
                prendas=prendas,
                telas=telas,
                acabados=acabadosAll,
                total=usd(total),
            )

        except Exception:
            # If there's an error show the alert
            return render_template(
                "calculator.html",
                prendas=prendas,
                telas=telas,
                acabados=acabadosAll,
                error=error,
            )

    # If there's no total calculated just render the empty form
    return render_template(
        "calculator.html", prendas=prendas, telas=telas, acabados=acabadosAll
    )


@app.route("/contact")
def contact():
    """Show contact page"""
    return render_template("contact.html")


@app.route("/")
def index():
    """Show about page"""
    return render_template("index.html")
