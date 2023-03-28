from django import forms
from django.forms import ModelForm
from .models import Rebate

class RebateForm(ModelForm):
    class Meta:
        model = Rebate
        fields = ('allocation_id','start_date','end_date')