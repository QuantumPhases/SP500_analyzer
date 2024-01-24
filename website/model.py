from sqlalchemy.sql import func
from . import db

class SP500_Realtime_Data(db.Model):
    __tablename__ = "SP500_Realtime_Data"
    id = db.Column(db.Integer, primary_key=True)  # Add this line for the primary key
    ticker = db.Column(db.String(255))
    company = db.Column(db.String(255))
    sector = db.Column(db.String(255))
    market_cap = db.Column(db.String(255))
    date = db.Column(db.Date)
    weekly_open = db.Column(db.Integer)
    weekly_close = db.Column(db.Integer)
    weekly_percentage = db.Column(db.Integer)
    weekly_volume = db.Column(db.Integer)
