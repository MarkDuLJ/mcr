from django.contrib import messages
from django.shortcuts import render
from .forms import AppointmentForm


def home(request):
    return render(request, 'job/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'job/about.html', {'title': 'About'})


def appointment(request):
    if request.method == 'POST':
        filled_form = AppointmentForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Appointment booked') \
                # = 'Thanks for booking! Engineer %s will visit you at %s !' % (
                # filled_form.cleaned_data['engineer'], filled_form.cleaned_data['date'],
                # )
        else:
            note = 'Appointment was not created, please try again'
        new_form = AppointmentForm()
        return render(request, 'job/appointment.html',
                      {'AppointmentForm': new_form})
    else:
        form = AppointmentForm()
        return render(request, 'job/appointment.html', {'AppointmentForm': form})
