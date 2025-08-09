from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    # tên công ty - cái này phải bắt buộc
    company = StringField('Công ty', validators=[
                          DataRequired(message="Tên công ty là bắt buộc.")])
    # vị trí mà bạn muốn apply - cái này phải bắt buộc
    position = StringField('Vị trí', validators=[
                           DataRequired(message="Vị trí là bắt buộc.")])
    # trạng thái - có options mặc địch
    status = SelectField('Trạng thái', choices=[
        ('pending', 'Đang chờ'),
        ('interviewing', 'Đang phỏng vấn'),
        ('rejected', 'Đã từ chối'),
        ('accepted', 'Đã nhận')
    ])
    # ngày nộp đơn - bắt buộc
    submission_date = DateField('Ngày nộp đơn', validators=[
                                DataRequired(message="Vui lòng chọn ngày.")])
    # ghi chú cho việc nộp đơn - không bắt buộc
    notes = TextAreaField('Ghi chú')
    submit = SubmitField('Lưu')
