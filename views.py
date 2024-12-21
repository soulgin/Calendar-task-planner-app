from django.shortcuts import render, redirect
from .models import Month, Task
from .forms import TaskForm, MonthForm
from django.contrib.auth import login
from .forms import SignUpForm

def view_month(request):
    if request.method == 'POST':
        form = MonthForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            try:
                month_obj = Month.objects.get(year=year, month=month)
            except Month.DoesNotExist:
                month_obj = Month(year=year, month=month, num_days=31, start_day=0)
                month_obj.save()
            tasks = Task.objects.filter(month=month_obj)
            return render(request, 'tasks/month.html', {'month': month_obj, 'tasks': tasks, 'form': form})
    else:
        form = MonthForm()
    return render(request, 'tasks/view_month.html', {'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_month')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('home')  # Redirect to the homepage (or another page)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

