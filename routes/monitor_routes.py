from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from models import Monitor, MonitorLog
from extensions import db

monitor_bp = Blueprint("monitor", __name__)


# Create a new monitor
@monitor_bp.route("/monitors", methods=["POST"])
@jwt_required()
def create_monitor():
    data = request.get_json()

    monitor = Monitor(
        name=data["name"],
        url=data["url"],
        check_interval=data.get("check_interval", 60)
    )

    db.session.add(monitor)
    db.session.commit()

    return jsonify({
        "message": "Monitor created successfully"
    }), 201


# Get all monitors
@monitor_bp.route("/monitors", methods=["GET"])
@jwt_required()
def get_monitors():
    monitors = Monitor.query.all()

    result = []

    for monitor in monitors:
        result.append({
            "id": monitor.id,
            "name": monitor.name,
            "url": monitor.url,
            "status": monitor.status,
            "http_status_code": monitor.http_status_code,
            "response_time": monitor.response_time,
            "check_interval": monitor.check_interval,
            "created_at": str(monitor.created_at),
            "last_checked": str(monitor.last_checked)
        })

    return jsonify(result), 200


# Get a single monitor by ID
@monitor_bp.route("/monitors/<int:id>", methods=["GET"])
@jwt_required()
def get_monitor(id):
    monitor = Monitor.query.get(id)

    if not monitor:
        return jsonify({
            "error": "Monitor not found"
        }), 404

    return jsonify({
        "id": monitor.id,
        "name": monitor.name,
        "url": monitor.url,
        "status": monitor.status,
        "http_status_code": monitor.http_status_code,
        "response_time": monitor.response_time,
        "check_interval": monitor.check_interval,
        "created_at": str(monitor.created_at),
        "last_checked": str(monitor.last_checked)
    }), 200


# Update a monitor
@monitor_bp.route("/monitors/<int:id>", methods=["PUT"])
@jwt_required()
def update_monitor(id):
    monitor = Monitor.query.get(id)

    if not monitor:
        return jsonify({
            "error": "Monitor not found"
        }), 404

    data = request.get_json() or {}

    monitor.name = data.get("name", monitor.name)
    monitor.url = data.get("url", monitor.url)
    monitor.check_interval = data.get(
        "check_interval",
        monitor.check_interval
    )

    db.session.commit()

    return jsonify({
        "message": "Monitor updated successfully"
    }), 200


# Delete a monitor
@monitor_bp.route("/monitors/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_monitor(id):
    monitor = Monitor.query.get(id)

    if not monitor:
        return jsonify({
            "error": "Monitor not found"
        }), 404

    db.session.delete(monitor)
    db.session.commit()

    return jsonify({
        "message": "Monitor deleted successfully"
    }), 200


# Get all monitor logs
@monitor_bp.route("/logs", methods=["GET"])
@jwt_required()
def get_logs():
    logs = MonitorLog.query.all()

    result = []

    for log in logs:
        result.append({
            "id": log.id,
            "monitor_id": log.monitor_id,
            "status": log.status,
            "http_status_code": log.http_status_code,
            "response_time": log.response_time,
            "checked_at": str(log.checked_at)
        })

    return jsonify(result), 200


# Get logs of a specific monitor
@monitor_bp.route("/logs/<int:monitor_id>", methods=["GET"])
@jwt_required()
def get_monitor_logs(monitor_id):
    logs = MonitorLog.query.filter_by(
        monitor_id=monitor_id
    ).all()

    result = []

    for log in logs:
        result.append({
            "id": log.id,
            "status": log.status,
            "http_status_code": log.http_status_code,
            "response_time": log.response_time,
            "checked_at": str(log.checked_at)
        })

    return jsonify(result), 200