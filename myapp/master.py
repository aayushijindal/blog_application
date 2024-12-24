from django.shortcuts import render, redirect
from .forms import *

  # Replace with your actual form import

def accounts(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data to the database
            return redirect('index')  # Redirect to the 'index' page after successful form submission
    else:
        form = AccountForm()

    # Fetch all groups to populate the dropdown
    groups = Group.objects.all()

    return render(request, 'master/accounts.html', {'form': form, 'groups': groups})


def groups(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'index' with your actual success URL
    else:
        form = GroupForm()

    return render(request, 'master/groups.html', {'form': form})

def items(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'index' with your actual success URL
    else:
        form = ItemForm()

    return render(request, 'master/items.html', {'form': form})


