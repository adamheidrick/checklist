# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CheckList(models.Model):
    _inherit = 'crm.lead'

    @api.depends("todo_checklist")
    def todo_progress(self):
        for rec in self:
            total_len = self.env["todo.checklist"].search_count([])
            check_list_len = len(rec.todo_checklist)
            if total_len != 0:
                rec.todo_progress = (check_list_len*100) / total_len

    todo_checklist = fields.Many2many("todo.checklist", string="Todo")
    todo_progress = fields.Float(compute=todo_progress, string="Progress", store=True, precompute=True, default=0.0)
    max_rate = fields.Integer(string="Maximum rate", default=100)


class TodoChecklist(models.Model):
    _name = "todo.checklist"
    _description = "Todo Checklist"

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")





