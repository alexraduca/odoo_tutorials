from odoo import fields, models

class TestModelTags(models.Model):
    _name = 'estate.property.tags'
    _description = 'Estate Property Tags'

    name = fields.Char('Name', required=True, translate=True)