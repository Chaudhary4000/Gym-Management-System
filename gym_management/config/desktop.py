# gym_management/config/desktop.py

from frappe import _

def get_data():
    return [
        {
            "module_name": "Gym Management",
            "category": "Modules",
            "label": _("Gym Management"),
            "color": "#FF5733",
            "icon": "octicon octicon-person",
            "type": "module",
            "description": "Manage Gym Members, Fees, Attendance"
        }
    ]