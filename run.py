from flask import Flask, send_from_directory
from config.db_config import init_db, mysql
from app.routes.order_routes import order_bp
from app.routes.dashboard_routes import dashboard_bp
from flask_cors import CORS

app = Flask(__name__, static_folder="frontend")
CORS(app)

init_db(app)

app.register_blueprint(order_bp)
app.register_blueprint(dashboard_bp)

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/receipt")
def receipt():
    return send_from_directory("frontend", "receipt.html")

@app.route("/test-db")
def test_db():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT 1")
    return {"message": "Database connected ✅"}

if __name__ == "__main__":
    app.run(debug=True)
