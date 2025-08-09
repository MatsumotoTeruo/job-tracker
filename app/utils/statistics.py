from collections import Counter
from app.models.job import Job


def get_job_statistics():
    jobs = Job.query.all()
    total = len(jobs)
    stats = {
        'total': total,
        'by_status': {},
        'percent_status': {}
    }

    if total == 0:
        return stats

    status_counts = Counter(job.status for job in jobs)
    stats['by_status'] = dict(status_counts)
    stats['percent_status'] = {
        status: round((count / total) * 100, 2)
        for status, count in status_counts.items()
    }

    return stats


def get_monthly_submission_counts():
    jobs = Job.query.all()
    monthly = Counter()

    for job in jobs:
        if job.submission_date:
            key = job.submission_date.strftime('%Y-%m')
            monthly[key] += 1

    return dict(monthly)
