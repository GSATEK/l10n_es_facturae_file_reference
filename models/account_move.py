# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    file_reference = fields.Char(string='Referencia de solicitud', copy=False)

    @api.model
    def create(self, vals):
        res = super(AccountMove, self).create(vals)
        if res.file_reference:
            for rec in res:
                for line in rec.invoice_line_ids:
                    line.write({'facturae_file_reference': rec.file_reference})
        return res


    @api.onchange('file_reference')
    def _onchange_file_reference(self):
        for rec in self:
            for line in rec.invoice_line_ids:
                line.write({'facturae_file_reference': rec.file_reference})


    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        if 'file_reference' in vals:
            for rec in self:
                for line in rec.invoice_line_ids:
                    line.write({'facturae_file_reference': rec.file_reference})
        return res
