# gym_management/config/gym_management.py

from frappe import _

def get_data():
    return [
        {
            "label": _("Members"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Gym Member",
                    "label": _("Gym Member"),
                    "description": _("Manage all gym members")
                },
                {
                    "type": "doctype", 
                    "name": "Membership Plan",
                    "label": _("Membership Plan")
                }
            ]
        },
        {
            "label": _("Fees & Payments"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Fee Collection",
                    "label": _("Fee Collection")
                }
            ]
        },
        {
            "label": _("Attendance"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Gym Attendance",
                    "label": _("Attendance")
                }
            ]
        },
        {
            "label": _("Reports"),
            "items": [
                {
                    "type": "report",
                    "name": "Member Report",
                    "label": _("Member Report"),
                    "doctype": "Gym Member"
                }
            ]
        }
    ]