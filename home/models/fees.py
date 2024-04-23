from django.db import models
from django.utils.translation import gettext as _

class Fee(models.Model):
    prev_sem_fee = models.IntegerField(_("Previous Semester Fee"),default=0,null=True)
    upcoming_sem_fee = models.IntegerField(_("Upcoming Semester Fee"),default=0,null=True)
    program = models.CharField(_("Academic Program"),max_length=50,default="",null=True,blank=True)

    def __str__(self):
        return self.program
    
    class Meta:
        app_label = "home"
        verbose_name = "Fee Details"
        verbose_name_plural = "Fee Details"