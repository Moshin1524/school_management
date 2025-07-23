from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Information'

    name = fields.Char(string='Full Name', required=True)
    employee_id = fields.Char(string='Employee ID', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    hire_date = fields.Date(string='Hire Date')
    institution_id = fields.Many2one('school.institution', string="Institution")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    teacher_image = fields.Binary(string="Photo")
    active = fields.Boolean(string='Active', default=True)

    @api.depends()
    def _compute_total_teachers(self):
        # This method returns the total number of teachers in the database
        countTeacher = self.env['school.teacher'].search_count([])
        for record in self:
            record.total_teachers = countTeacher

    @api.model
    def get_teacher_count(self):
        return self.search_count([])

