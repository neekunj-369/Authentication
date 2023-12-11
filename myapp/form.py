from django.forms import ModelForm
from .models import feature


class roomform(ModelForm):
    class Meta:
        model = feature
        fields = '__all__'
        # name= map
