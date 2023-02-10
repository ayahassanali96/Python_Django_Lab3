from django import forms
from .models import Catagory
class CategoryForm(forms.Form):
    name=forms.CharField(label='Category_name',initial='plapsls')


'''
class CatagoryForm2(forms.ModelForm):
    class Meta:
        model=Catagory
        fileds='__all__'
'''

