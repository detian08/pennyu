# -*- coding: utf-8 -*-
# pylint: disable=C0111,W0104
{
    'name': 'Pennyu - Portal User',
    'version': '11.0.1.0.1',
    'summary': 'Portal Sales',
    'description': """
    v 1.0
        author : Reza Akbar \n
        * Create groups for portal RWS
    v 1.1
        author : Hajiyanto Prakoso \n
        * Create groups for portal sales
    v 1.2
        Author : Saiful Rijal\n
        - Add new features:
            - Portal user groups RnP
    v 1.3
        author : Yusuf Danny \n
        * Create new group "Transporter"
    v 1.4
        author : Joenan Arkana \n
        * Create new group "Customer Inventory, Customer Payment, Customer All"
    """,
    'category': 'Generic Modules',
    'author': "Portcities Ltd, Arkana",
    'website': "https://arkana.co.id",
    'depends': [
        'sale_management', 
        'helpdesk', 
        'survey', 
        'sale_stock', 
        'stock_account', 
        'mrp',
    ],
    'data': [
        "security/portal_user_security.xml",
        "security/ir.model.access.csv",
        "views/account_invoice_views.xml",
        "views/stock_picking_views.xml",
        "views/product_template_views.xml",
        "views/sale_view.xml",
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
