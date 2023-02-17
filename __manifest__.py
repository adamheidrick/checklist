# -*- coding: utf-8 -*-
{
    'name': "Checklist",

    'summary': """
        This is a checklist module for Odoo.""",

    'description': """
        This is a checklist module for Odoo as per an interview technical assessment. This module should allow
        the user to add checkboxes for every lead in order to check individual progress. Every lead should have all
        the configured checkboxes. Checkboxes should be clickable without clicking edit before hand and saved 
        automatically. Progress should be visible through a progress bar which is shown over the list. 
        The progress bar should also be visible in the overview, in the KanBan board, for each lead. 
    """,

    'author': "Adam Heidrick",
    'website': "https://github.com/adamheidrick/checklist",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/checklist.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
