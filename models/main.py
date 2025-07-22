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

    @http.route('/school_dashboard/institution_data', type='json', auth='user')
    def institution_data(self, institution_id=None):
        domain = []
        if institution_id:
            domain = [('institution_id', '=', int(institution_id))]

        student_count = request.env['school.student'].search_count(domain)
        # Classes: unique class_ids from students
        # class_ids = request.env['school.student'].search(domain).mapped('class_id').filtered(lambda c: c)
        # class_count = len(class_ids)
        # Sections: unique section_ids from students
        # section_ids = request.env['school.student'].search(domain).mapped('section_id').filtered(lambda s: s)
        # section_count = len(section_ids)


        # working for the student, class and section count if institution selected or unselected
        # when select a institution it will show the count of student class and section under the institution assigned
        # if we select all institution it will show all the student assigned student class and section count
        students = request.env['school.student'].search(domain)
        if institution_id:
            class_count = len(students.mapped('class_id').filtered(lambda c: c))
            section_count = len(students.mapped('section_id').filtered(lambda s: s))
        else:
            # No institution filter → show total assigned unique classes & sections
            all_students = request.env['school.student'].search([])
            class_count = len(all_students.mapped('class_id').filtered(lambda c: c))
            section_count = len(all_students.mapped('section_id').filtered(lambda s: s))

        return {
            'student_count': student_count,
            'class_count': class_count,
            'section_count': section_count,
        }

    @http.route('/school_dashboard/institutions', type='json', auth='user')
    def get_institutions(self):
        institutions = request.env['school.institution'].search([])
        return {
            'institutions': [{'id': inst.id, 'name': inst.name} for inst in institutions]
        }