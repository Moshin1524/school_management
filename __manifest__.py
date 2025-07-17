{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage student information',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/students_views.xml',
        'views/teacher_views.xml',
        'views/configuration_views.xml',
        'views/menu.xml',
        'views/school_student_report.xml',
        'views/school_teacher_report.xml',
    ],
    'installable': True,
    'application': True,
}
