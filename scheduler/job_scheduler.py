from apscheduler.schedulers.background import BackgroundScheduler
from services.monitor_service import check_all_monitors
from datetime import datetime

scheduler = BackgroundScheduler()


def start_scheduler(app):
    print("Scheduler started...")

    def scheduled_job():
        with app.app_context():
            print(f"Running automatic monitor check... {datetime.now()}")
            check_all_monitors()

    scheduler.add_job(
        func=scheduled_job,
        trigger="interval",
        seconds=60,
        id="monitor_check_job"
    )

    scheduler.start()   