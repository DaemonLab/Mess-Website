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
    AllocationAutumn22,
    CatererBillsAutumn22,
    PeriodAutumn22,
    RebateAutumn22,
)
from .Semesters.autumn23 import (
    AllocationAutumn23,
    CatererBillsAutumn23,
    PeriodAutumn23,
    RebateAutumn23,
)
from .Semesters.spring23 import (
    AllocationSpring23,
    CatererBillsSpring23,
    PeriodSpring23,
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
