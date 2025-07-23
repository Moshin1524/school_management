from odoo import api, fields, models
class SchoolDashboardData(models.Model):
    _name = 'school.dashboard.data'
    _description = 'Dashboard Data'

    @api.model
    def get_dashboard_counts(self, institution_id=None, **kwargs):
        counts = {
            'student_count': 0,
            'teacher_count': 0,
            'class_count': 0,
            'section_count': 0,
        }
        if institution_id:
            domain = [('institution_id', '=', institution_id)]
            counts['student_count'] = self.env['school.student'].search_count(domain)
            counts['teacher_count'] = self.env['school.teacher'].search_count(domain)
            counts['class_count'] = self.env['school.class'].search_count(domain)
            counts['section_count'] = self.env['school.section'].search_count(domain)
        return counts

    @api.model
    def get_institutions(self, **kwargs):
        institutions = self.env['school.institution'].search([])
        return [{'id': inst.id, 'name': inst.name} for inst in institutions]