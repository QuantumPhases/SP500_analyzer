from flask import Blueprint, render_template, redirect, request, url_for, jsonify
import requests
import yfinance as yf
from .model import SP500_Realtime_Data
from datetime import datetime

views = Blueprint("views", __name__)

@views.route('/voo/api')
def vooapi():
    voo = yf.Ticker("VOO")
    historical_data = voo.history(period="1d")  # Fetch data for the last day

    if not historical_data.empty:
        close_date = historical_data.index[-1].strftime("%m-%d-%Y")
        latest_close_value = historical_data["Close"].iloc[-1]
        close_value = round(latest_close_value, 2)
    else:
        latest_close_date = "N/A"
        close_value = "N/A"

    return jsonify({"close_value": close_value, "close_date": close_date})

@views.route("/")
def main():
    sector_names = ["Communication Services", "Consumer Discretionary", "Consumer Staples", "Energy", "Financials", "Health Care", "Industrials", "Information Technology", "Materials", "Real Estate", "Utilities"]
    sector_data = {}

    for sector in sector_names:
        companies = SP500_Realtime_Data.query.filter_by(sector=sector).all()
        sector_data[sector] = companies
        
    return render_template("main.html", sector_names=sector_names, sector_data=sector_data)

@views.route("/documentation")
@views.route("/docs")
def docs():
    return render_template("docs.html")
