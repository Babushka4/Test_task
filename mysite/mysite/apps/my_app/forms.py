from django import forms


class UserForm(forms.Form):
    tank_id = forms.IntegerField(min_value=1, max_value=5)
    name = forms.CharField(min_length=2, max_length=20)
    liters = forms.IntegerField(min_value=1)
    comment = forms.CharField(min_length=1, max_length=100)