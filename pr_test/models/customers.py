from odoo import fields, models

class Customers(models.Model):
    _name = 'customers'
    _description = 'Customers'

    name = fields.Char('Name', required=True, translate=True)