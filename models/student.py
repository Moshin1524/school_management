from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Information'

    name = fields.Char(string='Full Name', required=True)
    roll_number = fields.Char(string='Roll Number', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    student_class = fields.Char(string='Class')
    section = fields.Selection([
        ('a', 'Section A'),
        ('b', 'Section B'),
        ('c', 'Section C'),
    ], string='Section')
    address = fields.Text(string='Address')
    student_image = fields.Binary(string="Photo")
    active = fields.Boolean(string='Active', default=True)
