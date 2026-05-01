from flask import Blueprint, jsonify
from app.services.dashboard_service import get_dashboard_data

dashboard_bp = Blueprint("dashboard_bp", __name__)

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    data = get_dashboard_data()
    return jsonify(data)