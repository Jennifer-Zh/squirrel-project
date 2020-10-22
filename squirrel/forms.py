from django import forms 
from django.forms import ModelForm
from .models import Squirrel

class DateInput(forms.DateInput): 
    input_type = "date" 

    def __init__ (self, **kwargs):
        kwargs["format"] = "%mm-%dd%Y"
        super().__init__(**kwargs)

class Form(forms.ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields["Date"].widget = DateInput() 
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

