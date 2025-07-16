from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Information'

    name = fields.Char(string='Full Name', required=True)
    employee_id = fields.Char(string='Employee ID', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    hire_date = fields.Date(string='Hire Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    teacher_image = fields.Binary(string="Photo")
    active = fields.Boolean(string='Active', default=True)

