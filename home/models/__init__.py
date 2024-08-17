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
from .Semesters.autumn22 import (
    RebateAutumn22,
)
from .Semesters.spring23 import (
    RebateSpring23,
)
from .students import (
    AllocationForm,
    LeftLongRebate,
    LeftShortRebate,
    LongRebate,
    Rebate,
    Scan,
    Student,
    TodayRebate,
    UnregisteredStudent,
)
from .allocation import Allocation, Period, Semester
from .bills import CatererBills, StudentBills
