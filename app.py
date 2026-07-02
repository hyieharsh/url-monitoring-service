from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from config import Config
from extensions import db, migrate

from models import Monitor, MonitorLog, User

from routes.monitor_routes import monitor_bp
from routes.auth_routes import auth_bp

from services.monitor_service import check_all_monitors
from services.email_service import send_email_alert

from scheduler.job_scheduler import start_scheduler

app = Flask(__name__)
app.config.from_object(Config)

# JWT Secret Key
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Initialize Extensions
db.init_app(app)
migrate.init_app(app, db)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(monitor_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return "URL Monitoring Service Running"


@app.route("/hello")
def hello():
    return "Hello"


@app.route("/run-check")
def run_check():
    check_all_monitors()
    return "All monitors checked."


@app.route("/test-email")
def test_email():
    monitor = Monitor.query.first()

    if monitor:
        send_email_alert(monitor)
        return "Test email sent."

    return "No monitors found."


if __name__ == "__main__":
    start_scheduler(app)
    app.run(debug=True, use_reloader=False)