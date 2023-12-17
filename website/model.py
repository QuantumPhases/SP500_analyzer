from sqlalchemy.sql import func
from . import db

class SP500_Columns_Key(db.Model):
    __tablename__ = "SP500_Columns_Key"
    id = db.Column(db.Integer, primary_key=True)  # Add this line for the primary key
    tickers = db.Column(db.String(255))
    company = db.Column(db.String(255))
    sectors = db.Column(db.String(255))
    market_cap = db.Column(db.String(255))
    monthly_volume = db.Column(db.Integer)
    weekly_volume = db.Column(db.Integer)