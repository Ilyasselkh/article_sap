{
    'name': "Article SAP",
    'version': '1.0.1',
    'category': 'ArticleSAP',
    'sequence' : -100,
    'application' : True,
    'installable': True,
    'license': 'LGPL-3',
    'depends': ['base','mail'],    
    'data':[
        'data/mail_template_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/article.xml',
        'views/derogation.xml',
        'views/deleted.xml',
    ]

}
