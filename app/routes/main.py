from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.forms import JobForm
from app.models import Job
from app.utils.statistics import get_job_statistics, get_monthly_submission_counts
from app import db
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # lấy tất cả công việc và hiển thị trang chủ
    status = request.args.get('status')
    if status:
        jobs = Job.query.filter_by(status=status).all()
    else:
        jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)


@main.route('/add', methods=['GET', 'POST'])
def add_job():
    # tạo form mới
    form = JobForm()
    # xử lý khi submit form
    if form.validate_on_submit():
        # tạo job mới từ dữ liệu form
        job = Job(
            company_name=form.company.data,
            position=form.position.data,
            status=form.status.data,
            submission_date=form.submission_date.data or datetime.now().date(),
            notes=form.notes.data
        )
        # lưu vào database
        db.session.add(job)
        db.session.commit()
        flash('Thêm công việc thành công!', 'success')
        # chuyển về trang chủ khi đã lưu vào database và hiện thông báo trạng thái thành công
        return redirect(url_for('main.index'))
    # hiển thị form nộp
    return render_template('add_job.html', form=form)


@main.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    # lấy công việc(jobs) từ database
    job = Job.query.get_or_404(job_id)
    # tạo form với dữ liệu hiện tại
    form = JobForm(obj=job)
    # xử lý khi submit form
    if form.validate_on_submit():
        # cập nhật thông tin công việc (job)
        job.company_name = form.company.data
        job.position = form.position.data
        job.status = form.status.data
        job.submission_date = form.submission_date.data
        job.notes = form.notes.data
        # lưu thay đổi
        db.session.commit()
        flash('Cập nhật công việc thành công!', 'success')
        # chuyển về lại trang chủ
        return redirect(url_for('main.index'))
    return render_template('edit_job.html', form=form)


@main.route('/delete/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    flash('Đã xóa công việc.', 'success')
    return redirect(url_for('main.index'))


@main.route('/statistics')
def statistics():
    stats = get_job_statistics()
    monthly = get_monthly_submission_counts()
    return render_template('statistics.html', stats=stats, monthly=monthly)
