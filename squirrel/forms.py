from django.forms import ModelForm
from .models import Squirrel


class Form(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

