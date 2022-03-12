from django.shortcuts import render
from .models import MilkTank, Fulling
from django.views.generic import TemplateView
from .forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


def main_window(request):
    if request.method == 'POST':

        userform = UserForm(request.POST or None)
        if userform.is_valid():

            # data extracting
            current_name = userform.cleaned_data['name']
            current_fulling = userform.cleaned_data['liters']
            current_comment = userform.cleaned_data['comment']
            tank_id = userform.cleaned_data['tank_id']

            # save data
            fulling_sample = Fulling(milk_tank_id=tank_id, name=current_name,
                                    liters=current_fulling, comment=current_comment)
            current_tank = MilkTank.objects.filter(id=tank_id)[0]

            # проверка на переполненность
            if current_tank.fullness < 300:
                if current_tank.fullness + current_fulling > 300:
                    return HttpResponse("Выбранное число литров переполнит цистерну")

                current_tank.fulling(current_fulling)
                current_tank.save()
                fulling_sample.save()
            else:
                return HttpResponse("Выбранная цистерна переполненна")

            return HttpResponseRedirect("/")

        else:
            return HttpResponse("Invalid data")
    else:
        form = UserForm()
        tank_info = MilkTank.objects.all()
        fulling_info = Fulling.objects.order_by('name')
        return render(request, 'shablon.html', {'milk_tank': tank_info,
                                                'fulling_info': fulling_info,
                                                'form': form})
