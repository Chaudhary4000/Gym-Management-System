import frappe
from frappe.model.document import Document
class GymMembership(Document):

    def onload(self):
        return
        frappe.msgprint(f"Welcome {self.member}!")
