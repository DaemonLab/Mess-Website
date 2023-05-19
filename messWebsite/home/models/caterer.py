from django.db import models
from django.utils.translation import gettext as _


class Caterer(models.Model):
    """
    Stores All Caterers on cafeteria page
    """
    name = models.CharField(_("Caterer Name"), max_length=50,
                            help_text="The text in this text field contains the caterer name.")
    upper_description = models.TextField(
        _("Upper Description"), help_text="This contains the description of the respective caterer that will show on the upper side.")
    sheet_url = models.URLField(
        _("Menu URL"), help_text="This contains the google sheets url link for the respective caterers menu.")
    lower_description = models.TextField(
        _("Lower Discription"), default="", help_text="This contains the description of the respective caterer that will show on the lower side.")
    student_limit = models.IntegerField(
        _("Caterers Student Limit"), default=0, help_text="The limit on number of students it can have")

    def __str__(self):
        return "Caterer " + self.name

    class Meta:
        verbose_name = "Caterer"
        verbose_name_plural = "Caterers"

class CatererBillsSpring(models.Model):
    """
    Storing the Bills of the Caterers for the Spring Semester
    """
    Caterer = models.ForeignKey(Caterer,max_length=30, on_delete=models.SET_NULL, null=True)

    januaryBill = models.IntegerField(_("January Bill"),default=0, null=True)
    feburaryBill = models.IntegerField(_("Feburary Bill"),default=0, null=True)
    marchBill = models.IntegerField(_("March Bill"),default=0, null=True)
    aprilBill = models.IntegerField(_("April Bill"),default=0, null=True)
    mayBill = models.IntegerField(_("May Bill"),default=0, null=True)
    juneBill = models.IntegerField(_("June Bill"),default=0, null=True)

    def __str__(self):
        return str(self.Caterer.name)

    class Meta:
        verbose_name = "Caterer Bill Spring Semester"
        verbose_name_plural = "Caterer Bills Spring Semester"

class CatererBillsAutumn(models.Model):
    """
    Storing the Bills of the Caterers for the Autumn Semester
    """
    Caterer = models.ForeignKey(Caterer,max_length=30,on_delete=models.SET_NULL, null=True)

    julyBill = models.IntegerField(_("July Bill"),default=0, null=True)
    augustBill = models.IntegerField(_("August Bill"),default=0, null=True)
    septemberBill = models.IntegerField(_("September Bill"),default=0, null=True)
    octoberBill = models.IntegerField(_("October Bill"),default=0, null=True)
    novemberBill = models.IntegerField(_("November Bill"),default=0, null=True)
    decemberBill = models.IntegerField(_("December Bill"),default=0, null=True)

    def __str__(self):
        return str(self.Caterer.name)

    class Meta:
        verbose_name = "Caterer Bill Autumn Semester"
        verbose_name_plural = "Caterer Bills Autumn Semester"
