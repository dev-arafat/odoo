from odoo import api, fields, models, exceptions,_


class accountMove(models.Model):
    _inherit = "account.move"

    def action_cash_payment(self):

        # payment = self.env['account.payment.register'].with_context(active_model='account.move')
        journal_id = self.env['account.journal'].search([('name', '=', 'Cash')])
        # wiz_dict = self.with_context({'default_journal_id': journal_id.id}).action_register_payment()
        #wiz_id = self.env['account.payment.register'].search([('communication', '=', self.name)])
        self.env['account.payment.register'] \
            .with_context(active_ids=self.ids, active_model='account.move') \
            .create({'journal_id':journal_id.id}) \
            ._create_payments()
        # return wiz_id.create_payments()

