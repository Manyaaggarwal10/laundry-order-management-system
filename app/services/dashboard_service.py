from config.db_config import mysql

def get_dashboard_data():
    cursor = mysql.connection.cursor()

    # Total orders
    cursor.execute("SELECT COUNT(*) FROM orders")
    total_orders = cursor.fetchone()[0]

    # Total revenue
    cursor.execute("SELECT SUM(total_amount) FROM orders")
    total_revenue = cursor.fetchone()[0] or 0

    # Status breakdown
    cursor.execute("SELECT status, COUNT(*) FROM orders GROUP BY status")
    result = cursor.fetchall()

    status_data = {row[0]: row[1] for row in result}

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "status_breakdown": status_data
    }