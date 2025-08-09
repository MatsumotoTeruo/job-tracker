from flask import Blueprint, jsonify
from app.models import Job

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/jobs')
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])
