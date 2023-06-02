'''
The `__init__.py` file is used to mark a directory as a Python package, making it possible to import modules and sub-packages from that directory
'''


from .cafeteria import Cafeteria
from .caterer import Caterer
from .contacts import Contact
from .home import About, Carousel, Update
from .links import Form
from .rules import Rule, ShortRebate
from .students import Student, Scan, Rebate, LongRebate, UnregisteredStudent, TodayRebate, LeftLongRebate
from .Semesters.autumn22 import PeriodAutumn22, AllocationAutumn22, RebateAutumn22, CatererBillsAutumn22
from .Semesters.spring23 import PeriodSpring23, AllocationSpring23, RebateSpring23, CatererBillsSpring23
from .Semesters.autumn23 import PeriodAutumn23, AllocationAutumn23, RebateAutumn23, CatererBillsAutumn23
