from flask import Blueprint, request, jsonify
from app.services.billing_service import calculate_total
from app.services.order_service import create_order
from app.services.order_service import get_orders
from app.services.order_service import update_order_status

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/orders", methods=["GET"])
def get_orders_api():
    status = request.args.get("status")
    phone = request.args.get("phone")

    filters = {
        "status": status,
        "phone": phone
    }

    orders = get_orders(filters)

    return jsonify(orders)


@order_bp.route("/orders", methods=["POST"])
def create_order_api():
    data = request.get_json()

    # Validate input
    if not data.get("customer_name") or not data.get("phone"):
        return jsonify({"error": "Missing customer details"}), 400

    if not data.get("garments"):
        return jsonify({"error": "No garments provided"}), 400

    # Calculate bill
    total_amount = calculate_total(data["garments"])

    # Save order
    order_id = create_order(data, total_amount)

    return jsonify({
        "order_id": order_id,
        "total_amount": total_amount,
        "status": "RECEIVED"
    })


@order_bp.route("/orders/<int:order_id>/status", methods=["PUT"])
def update_status_api(order_id):
    role = request.args.get("role")  # 👈 NEW

    if role != "owner":
        return jsonify({"error": "Only store owner can update status"}), 403

    data = request.get_json()
    status = data.get("status")

    valid_status = ["RECEIVED", "PROCESSING", "READY", "DELIVERED"]

    if status not in valid_status:
        return jsonify({"error": "Invalid status"}), 400

    updated = update_order_status(order_id, status)

    if updated == 0:
        return jsonify({"error": "Order not found"}), 404

    return jsonify({"message": "Status updated successfully"})