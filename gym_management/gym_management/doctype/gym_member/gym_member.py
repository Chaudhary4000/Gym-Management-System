import frappe
from frappe.model.document import Document

class GymMember(Document):

    def onload(self):
        frappe.msgprint(f"Welcome {self.custom_full_name}!")


#         def validate(self):
#     pass

# def before_save(self):
#     pass
# # def after_insert(self):
#     pass

# def on_update(self):
#     pass

# def on_submit(self):
#     pass

# def on_cancel(self):
#     pass