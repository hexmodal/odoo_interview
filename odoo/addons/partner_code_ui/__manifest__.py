{
    'name': 'Partner Code UI',
    'version': '17.0.1.0.0',
    'depends': ['base', 'web', 'contacts'],
    'data': [
        'views/res_partner_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'static/src/js/customer_code_field.js',
            'static/src/xml/customer_code_field.xml'
        ]
    }
}
