# -*- coding: utf-8 -*-
{
    
    # App information
    'name': 'Inventory Age Report and Break Down Report',
    'version': '11.0',
    'category': 'stock',
    'license': 'OPL-1',
    'summary' : 'Decrease your inventory  obsolescence risk with Inventory Age & Break Down report. You can generate both the report with just few clicks either Warehouse wise or location wise .',
   
   # Author
    'author': 'Emipro Technologies Pvt. Ltd.',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',   
    'website': 'http://www.emiprotechnologies.com/',
    
    
     # Odoo Store Specific   z`
    'images': ['static/description/Inventory-Age-Report-and-Break-down-Report-Cover.jpg'],
    
      
    
    # Dependencies    
    'depends': ['sale', 'stock', 'sale_stock', 'purchase'],
    'data':[
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/mail_template_data.xml',
        'wizard/inventory_age_report_ept_views.xml',
        'view/res_compay_views.xml',
        'wizard/inventory_age_breakdown_report_views.xml',
        'data/report_paperformat.xml',
        'wizard/inventory_age_report_pdf.xml'
            ],
            
            
    # Technical        
    'external_dependencies' : {'python' : ['xlwt'], },
    'installable': True,
    'auto_install': False,
    'application' : True,
    'active': False,
    'live_test_url':'http://www.emiprotechnologies.com/free-trial?app=inventory-report-ept&version=11',
    'price': 99.00,
    'currency': 'EUR',  

}
