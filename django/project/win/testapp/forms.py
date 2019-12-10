from django import forms  
from testapp.models import emp 
class EmployeeForm(forms.ModelForm):
    
    class Meta:  
        model = emp  
        fields = "__all__"  