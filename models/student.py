from odoo import models, fields, api

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
    # joining relation operations here
    class_id = fields.Many2one('school.class', string='Class')
    section_id = fields.Many2one('school.section', string='Section')
    institution_id = fields.Many2one('school.institution', string='Institution')
    address = fields.Text(string='Address')
    student_image = fields.Binary(string="Photo")
    active = fields.Boolean(string='Active', default=True)

    # Computed field to get total student count
    total_students = fields.Integer(string='Total Students', compute='_compute_total_students')

    @api.depends()
    def _compute_total_students(self):
        # This method returns the total number of students in the database
        count = self.env['school.student'].search_count([])
        for record in self:
            record.total_students = count

    @api.model
    def get_student_count(self):
        return self.search_count([])
