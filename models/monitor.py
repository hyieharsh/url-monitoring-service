from extensions import db
from datetime import datetime


class Monitor(db.Model):
    __tablename__ = "monitors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), default="ACTIVE")
    check_interval = db.Column(db.Integer, default=60)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_checked = db.Column(db.DateTime)

    http_status_code = db.Column(db.Integer)
    response_time = db.Column(db.Float)