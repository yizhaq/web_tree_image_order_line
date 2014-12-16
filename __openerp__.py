{
    "name" : "Product Image",
    "version" : "0.1",
    "author" : "Stefan Reisich, Rove.design GmbH",
    "website" : "http://www.rove.de/",
    "description": """
This Module overwrites openerp.web.list.Binary field to show the product image in the listview. A new column with product image is added.
    """,
    "depends" : [
                 "sale",
                 "sale_stock",
                 "product",
                 "stock"
    ],
    'js': [
           'static/src/js/view_list.js'
    ],
    "data": [
        'views/product_view.xml'
    ],
    'installable': True,
    "active": False,
}
