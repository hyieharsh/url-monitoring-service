import requests
import time
from datetime import datetime
from models import Monitor, MonitorLog
from extensions import db
from services.email_service import send_email_alert


def check_url(url):
    try:
        # Start timer
        start_time = time.time()

        # Send request
        response = requests.get(url, timeout=10)

        # Stop timer
        end_time = time.time()

        # Calculate response time in milliseconds
        response_time = (end_time - start_time) * 1000

        # Determine website status
        if response.status_code == 200:
            status = "UP"
        else:
            status = "DOWN"

        # Return status, HTTP status code, and response time
        return (
            status,
            response.status_code,
            round(response_time, 2)
        )

    except Exception:
        return "DOWN", None, None


def check_all_monitors():
    monitors = Monitor.query.all()

    for monitor in monitors:
        # Save previous status
        previous_status = monitor.status

        # Check website
        status, http_status_code, response_time = check_url(
            monitor.url
        )

        # Update monitor table
        monitor.status = status
        monitor.http_status_code = http_status_code
        monitor.response_time = response_time
        monitor.last_checked = datetime.utcnow()

        # Save every check into monitor_logs table
        log = MonitorLog(
            monitor_id=monitor.id,
            status=status,
            http_status_code=http_status_code,
            response_time=response_time
        )

        db.session.add(log)

        # Send email only when status changes from UP to DOWN
        if previous_status == "UP" and status == "DOWN":
            send_email_alert(monitor)

    # Save all changes
    db.session.commit()