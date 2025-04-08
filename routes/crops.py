from flask import Blueprint, request, jsonify
from config.postgres_config import WORKER_CONFIG, AUDITOR_CONFIG
import psycopg2


crops_bp = Blueprint('crops', __name__)

def get_db_connection():
    return psycopg2.connect(**WORKER_CONFIG)

@crops_bp.route('/api/crops', methods=['POST'])
def register_crop():
    data = request.get_json()

    field_id = data.get('field_id')
    crop_type = data.get('crop_type')
    planting_date = data.get('planting_date')
    harvest_date = data.get('harvest_date')
    status = data.get('status')

    if not all([field_id,crop_type, planting_date, harvest_date, status]):
        return jsonify({"error": "Missing requeris fields"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO crops (
                    field_id,
                    crop_type,
                    planting_date,
                    harvest_date,
                    status
                    )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING crop_id;
        """, (field_id, crop_type, planting_date, harvest_date, status)
        )
        crop_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'message':'Crop registered successfully', 'crop_id': crop_id}),201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    