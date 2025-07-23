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
        'views/dashboard_views.xml',
        'views/custom_dashboard.xml',
    ],
'assets': {
    'web.assets_backend': [
        'student_information/static/src/js/school_dashboard.js',
        'student_information/static/src/xml/school_dashboard_templates.xml',
        'student_information/static/src/js/custom_dashboard.js',
        'student_information/static/src/xml/custom_dashboard_template.xml',
    ],

},


    'installable': True,
    'application': True,
}
