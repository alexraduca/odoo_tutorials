from odoo import fields, models
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char('Title', required=True, translate=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    customer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tags_ids = fields.Many2many('estate.property.tags', string='Tags')
    property_id = fields.Many2one('estate.property', string='Property')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        string='Status',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        default='new',
        help='Status of the property',
        required=True,
        copy=False
    )
    description = fields.Char('Description', required=True, translate=True)
    postcode = fields.Char('Postcode', required=True)
    date_availability = fields.Date('Available From', copy=False, default=(fields.Date.today() + relativedelta(months=3)).strftime('%Y-%m-%d'))
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms', required=True, default=2)
    living_area = fields.Integer('Living Area (sqm)', required=True)
    facades = fields.Integer('Number of Facades', required=True)
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'),('south', 'South'),('east', 'East'),('west', 'West')],
        help='Orientation of the garden'
    )
