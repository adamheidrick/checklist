# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CheckList(models.Model):
    _inherit = 'crm.lead'
    todo_checklist = fields.Many2many("todo.checklist", string="Todo")


class TodoChecklist(models.Model):
    _name = "todo.checklist"
    _description = "Todo Checklist"

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")





