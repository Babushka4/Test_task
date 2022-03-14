from django.shortcuts import render
from .models import MilkTank, Fulling, Worker
from django.views.generic import TemplateView
from .forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import redirect


def main_window(request):
    if request.method == 'POST':

        userform = UserForm(request.POST or None)
        if userform.is_valid():

            # data extracting
            current_name = userform.cleaned_data['Имя_заливающего']
            current_fulling = userform.cleaned_data['Литры']
            current_comment = userform.cleaned_data['Комментарий']
            tank_id = userform.cleaned_data['Номер_цистерны']

            if Worker.objects.filter(name=current_name).exists():
                current_worker = Worker.objects.filter(name=current_name)[0]
            else:
                return HttpResponse("Работника не существует")

            # save data
            fulling_sample = Fulling(milk_tank_id=tank_id, name_id=current_worker.id,
                                    liters=current_fulling, comment=current_comment)
            current_tank = MilkTank.objects.filter(id=tank_id)[0]

            # проверка на опережение в заполнении остальных цистерн
            is_fuller_then_other = False
            tanks_data = MilkTank.objects.exclude(id=tank_id)
            for tank in tanks_data:
                if tank.fullness < current_tank.fullness - 20:
                    is_fuller_then_other = True

            # проверка на переполненность
            if current_tank.fullness < 300:
                if current_tank.fullness + current_fulling > 300:
                    return HttpResponse("Выбранное число литров переполнит цистерну")
                if is_fuller_then_other:
                    return HttpResponse("Выбранная цистерна опережает остальные")

                current_tank.fulling(current_fulling)
                current_tank.save()
                fulling_sample.save()
            else:
                return HttpResponse("Выбранная цистерна переполненна")

            return redirect("/", {})

        else:
            return HttpResponse("Invalid data")
    else:
        form = UserForm()
        tank_info = MilkTank.objects.all()
        fulling_info = Fulling.objects.order_by('name')
        return render(request, 'shablon.html', {'milk_tank': tank_info,
                                                'fulling_info': fulling_info,
                                                'form': form})


def show_all_fulls(request):
    fulling_info = Fulling.objects.order_by('name')
    return render(request, 'shablon_all_fulls.html', {'fulling_info': fulling_info})
