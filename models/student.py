from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

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

    @api.model
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('age') is not None and vals['age'] < 12:
                raise UserError("❌ Age Error: Student age cannot be under 12.")
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('age') is not None and vals['age'] < 12:
            raise UserError("❌ Age Error: Student age cannot be under 12.")
        return super().write(vals)

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age is not None and rec.age < 12:
                raise UserError("❌ Age Error: Student age cannot be under 12.")

    # @api.onchange('class_id')
    # def _onchange_class_id(self):
    #     if self.class_id:
    #         self.institution_id = self.class_id.institution_id
    #
    # @api.onchange('section_id')
    # def _onchange_section_id(self):
    #     if self.section_id:
    #         self.institution_id = self.section_id.institution_id

    @api.onchange('institution_id')
    def _onchange_institution_id(self):
        domain = {}
        if self.institution_id:
            domain['class_id'] = [('institution_id', '=', self.institution_id.id)]
            domain['section_id'] = [('institution_id', '=', self.institution_id.id)]
            # Clear old selection if mismatched
            self.class_id = False
            self.section_id = False
        return {'domain': domain}

