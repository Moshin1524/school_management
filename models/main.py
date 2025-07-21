from odoo import http
from odoo.http import request

class SchoolDashboardController(http.Controller):

    @http.route('/school_dashboard/student_count', type='json', auth='user')
    def student_count(self):
        countStudent = request.env['school.student'].search_count([])
        return {'count': countStudent}

    @http.route('/school_dashboard/teacher_count', type='json', auth='user')
    def teacher_count(self):
        countTeacher = request.env['school.teacher'].search_count([])
        return {'count': countTeacher}