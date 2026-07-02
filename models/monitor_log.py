from extensions import db
from datetime import datetime


class MonitorLog(db.Model):
    __tablename__ = "monitor_logs"

    id = db.Column(db.Integer, primary_key=True)

    monitor_id = db.Column(
        db.Integer,
        db.ForeignKey("monitors.id"),
        nullable=False
    )

    status = db.Column(db.String(20))
    http_status_code = db.Column(db.Integer)
    response_time = db.Column(db.Float)
    checked_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )