from odoo import fields, models

class TestModelType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char('Name', required=True, translate=True)