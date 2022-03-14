from django import forms


class UserForm(forms.Form):
    Номер_цистерны = forms.IntegerField(min_value=1, max_value=5)
    Имя_заливающего = forms.CharField(min_length=2, max_length=20)
    Литры = forms.IntegerField(min_value=1)
    Комментарий = forms.CharField(min_length=1, max_length=100)