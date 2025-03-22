"""
The `__init__.py` file is used to mark a directory as a Python package, making it possible to import modules and sub-packages from that directory
"""

from .cafeteria import Cafeteria
from .caterer import Caterer
from .contacts import Contact
from .fees import Fee
from .home import About, Carousel, Update
from .links import Form
from .rules import Rule, ShortRebate
from .students import (
    AllocationForm,
    LeftLongRebate,
    LeftShortRebate,
    LongRebate,
    Rebate,
    Scan,
    Student,
    UnregisteredStudent,
)
from .allocation import Allocation, Period, Semester
from .bills import CatererBills, StudentBills
from .menu import Menu
from .SDC import SDC
