from django.shortcuts import render, redirect
from .models import Add_task
from .forms import AddtaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def tasks(request):
    todo = Add_task.objects.all()
    form = AddtaskForm()
    if request.method == 'POST':
        form = AddtaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddtaskForm()
        
    task_dict = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'index.html', task_dict)


def finish(request, id):
    finishitem = Add_task.objects.get(id=id)
    finishitem.delete()
    return redirect('/')

def update(request, id):
    upd_item = Add_task.objects.get(id=id)
    form = AddtaskForm(instance=upd_item)

    if request.method == 'POST':
        up_form = AddtaskForm(request.POST, instance=upd_item)
        if up_form.is_valid():
            up_form.save()
            return redirect('/')

    upd_form = {
        'form': form,
        'upd_item': upd_item
    }

    return render(request, 'update.html', upd_form)