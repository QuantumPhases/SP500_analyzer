from flask import Blueprint, render_template, redirect, request, url_for
from .model import SP500_Columns_Key

views = Blueprint("views", __name__)

@views.route("/")
def main():
    sector_names = ["Communication Services", "Consumer Discretionary", "Consumer Staples", "Energy", "Financials", "Health Care", "Industrials", "Information Technology", "Materials", "Real Estate", "Utilities"]
    sector_data = {}

    for sector in sector_names:
        companies = SP500_Columns_Key.query.filter_by(sector=sector).all()
        sector_data[sector] = companies
        
    return render_template("main.html", sector_names=sector_names, sector_data=sector_data)