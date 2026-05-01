from config.db_config import mysql
import json

def create_order(data, total_amount):
    cursor = mysql.connection.cursor()

    query = """
    INSERT INTO orders (customer_name, phone, garments, total_amount, status)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        data["customer_name"],
        data["phone"],
        json.dumps(data["garments"]),  # store as JSON string
        total_amount,
        "RECEIVED"
    ))

    mysql.connection.commit()

    return cursor.lastrowid

def get_orders(filters):
    cursor = mysql.connection.cursor()

    query = "SELECT * FROM orders WHERE 1=1"
    params = []

    if filters.get("status"):
        query += " AND status=%s"
        params.append(filters["status"])

    if filters.get("phone"):
        query += " AND phone=%s"
        params.append(filters["phone"])

    cursor.execute(query, tuple(params))
    results = cursor.fetchall()

    columns = [col[0] for col in cursor.description]

    orders = []
    for row in results:
        order = dict(zip(columns, row))
        orders.append(order)

    return orders

def update_order_status(order_id, status):
    cursor = mysql.connection.cursor()

    query = "UPDATE orders SET status=%s WHERE id=%s"
    cursor.execute(query, (status, order_id))

    mysql.connection.commit()

    return cursor.rowcount


