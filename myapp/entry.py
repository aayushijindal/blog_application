from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *
from .master import *
from .models import *


from django.contrib import messages


def cash_entry(request):
    if request.method == 'POST':
        form = CashentryForm(request.POST)
        if form.is_valid():
            return redirect('cashentryform')  # Replace 'index' with your actual success URL
    else:
        form = CashentryForm()

    # Fetching accounts from the Account model
    accounts = Account.objects.all()  # Query to get all accounts

    return render(request, 'entry/cash_entry.html', {'form': form, 'accounts': accounts})


def cashentryform(request):
    if request.method == 'POST':
        form = Cashentryformmain(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successful save
    else:
        form = Cashentryformmain()  # Create a new form instance if not a POST request
    
    accounts = Account.objects.all()
    
    return render(request, 'entry/cashentryform.html', {'form': form, 'accounts': accounts})

def sauda_purchase(request):
    if request.method == 'POST':
        form = SaudaPurchase(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successful save
    else:
        form = SaudaPurchase()  # Create a new form instance if not a POST request
    
    accounts = Account.objects.all()
    items = Item.objects.all()
    
    return render(request, 'entry/sauda_purchase.html', {'form': form, 'accounts': accounts, 'items': items})


def sauda_sales(request):
    if request.method == 'POST':
        form = SaudaSalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successful save
    else:
        form = SaudaSalesForm()  # Create a new form instance if not a POST request
    
    accounts = Account.objects.all()
    items = Item.objects.all()
    
    return render(request, 'entry/sauda_sales.html', {'form': form, 'accounts': accounts, 'items': items})


def sales(request):
    if request.method == 'POST':
        form = SalesUpForm(request.POST)
        if form.is_valid():
            sales = form.save(commit=False)
            sales.save()

            # Process table data
            table_data = zip(
                request.POST.getlist('sr'),
                request.POST.getlist('item_name'),
                request.POST.getlist('sizes'),
                request.POST.getlist('pcs'),
                request.POST.getlist('quantity'),
                request.POST.getlist('b_rate'),
                request.POST.getlist('rate'),
                request.POST.getlist('amount')
            )
            for sr, item_name, sizes, pcs, quantity, b_rate, rate, amount in table_data:
                table_instance = Table(
                    table_entry=sales,
                    sr=sr,
                    item_name=item_name,
                    sizes=sizes,
                    pcs=pcs,
                    quantity=quantity,
                    b_rate=b_rate,
                    rate=rate,
                    amount=amount,
                )
                table_instance.save()

            # Process another model data (assuming it's similar to Table model fields)
            another_model_data = zip(
                request.POST.getlist('marka'),
                request.POST.getlist('transport'),
                request.POST.getlist('ref_no'),
                request.POST.getlist('lr_no'),
                request.POST.getlist('bill_no'),
                request.POST.getlist('packing'),
                request.POST.getlist('gst'),
                request.POST.getlist('tcs'),
                request.POST.getlist('tds'),
                request.POST.getlist('other'),
                request.POST.getlist('net_rtgs'),
                request.POST.getlist('net_diff'),
                request.POST.getlist('total')
            )
            for marka,transport,ref_no,lr_no,bill_no,packing,gst,tcs,tds,other,net_rtgs,net_diff,total in another_model_data:
                another_model_instance = SalesDown(
                    salesup=sales,  # Assuming AnotherModel has a ForeignKey to Sales
                    marka=marka,
                    transport=transport,
                    ref_no=ref_no,
                    lr_no=lr_no,
                    bill_no=bill_no,
                    packing=packing,
                    gst=gst,
                    tcs=tcs,
                    tds=tds,
                    other=other,
                    net_rtgs=net_rtgs,
                    net_diff=net_diff,
                    total=total,
                )
                another_model_instance.save()

            return redirect('index')  # Replace 'index' with your actual success URL
        else:
            # Form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = SalesUpForm()

    accounts = Account.objects.all()
    account2 = Account.objects.filter(type='Sale')
    items = Item.objects.all()

    return render(request, 'entry/sales.html', {'form': form, 'accounts': accounts, 'account2': account2, 'items': items})

def purchase(request):
    if request.method == 'POST':
        form = PurchaseUpForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.save()

            # Process table data
            table_data = zip(
                request.POST.getlist('sr'),
                request.POST.getlist('item_name'),
                request.POST.getlist('sizes'),
                request.POST.getlist('pcs'),
                request.POST.getlist('quantity'),
                request.POST.getlist('b_rate'),
                request.POST.getlist('rate'),
                request.POST.getlist('amount')
            )
            for sr, item_name, sizes, pcs, quantity, b_rate, rate, amount in table_data:
                table_instance = Tablenew(
                    table_entry=purchase,
                    sr=sr,
                    item_name=item_name,
                    sizes=sizes,
                    pcs=pcs,
                    quantity=quantity,
                    b_rate=b_rate,
                    rate=rate,
                    amount=amount,
                )
                table_instance.save()

            # Process another model data (assuming it's similar to Table model fields)
            another_model_data = zip(
                request.POST.getlist('marka'),
                request.POST.getlist('transport'),
                request.POST.getlist('ref_no'),
                request.POST.getlist('lr_no'),
                request.POST.getlist('bill_no'),
                request.POST.getlist('packing'),
                request.POST.getlist('gst'),
                request.POST.getlist('tcs'),
                request.POST.getlist('tds'),
                request.POST.getlist('other'),
                request.POST.getlist('net_rtgs'),
                request.POST.getlist('net_diff'),
                request.POST.getlist('total')
            )
            for marka,transport,ref_no,lr_no,bill_no,packing,gst,tcs,tds,other,net_rtgs,net_diff,total in another_model_data:
                another_model_instance = PurchaseDown(
                    purchaseup=purchase,  # Assuming AnotherModel has a ForeignKey to Sales
                    marka=marka,
                    transport=transport,
                    ref_no=ref_no,
                    lr_no=lr_no,
                    bill_no=bill_no,
                    packing=packing,
                    gst=gst,
                    tcs=tcs,
                    tds=tds,
                    other=other,
                    net_rtgs=net_rtgs,
                    net_diff=net_diff,
                    total=total,
                )
                another_model_instance.save()

            return redirect('index')  # Replace 'index' with your actual success URL
        else:
            # Form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = PurchaseUpForm()

    accounts = Account.objects.all()
    account2 = Account.objects.filter(type='Purchase')
    items = Item.objects.all()

    return render(request, 'entry/purchase.html', {'form': form, 'accounts': accounts, 'account2': account2, 'items': items})


def jventry(request):
    if request.method == 'POST':
        form = JVentryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successful save
        else:
            # Form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = JVentryForm()  # Create a new form instance if not a POST request

    accounts = Account.objects.all()

    return render(request, 'entry/jventry.html', {'form': form, 'accounts': accounts})


def production(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successful save
        else:
            # Form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = ProductionForm()  # Create a new form instance if not a POST request

    accounts = Account.objects.all()
    items = Item.objects.all()

    return render(request, 'entry/production.html', {'form': form, 'accounts': accounts, 'items': items})


def job_rec(request):
    if request.method == 'POST':
        form = JobRecForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.save()

            # Process table data
            table_data = zip(
                request.POST.getlist('sr'),
                request.POST.getlist('item_name'),
                request.POST.getlist('sizes'),
                request.POST.getlist('pcs'),
                request.POST.getlist('quantity'),
                request.POST.getlist('b_rate'),
                request.POST.getlist('rate'),
                request.POST.getlist('amount')
            )
            for sr, item_name, sizes, pcs, quantity, b_rate, rate, amount in table_data:
                table_instance = TableJobRec(
                    table_entry=purchase,
                    sr=sr,
                    item_name=item_name,
                    sizes=sizes,
                    pcs=pcs,
                    quantity=quantity,
                    b_rate=b_rate,
                    rate=rate,
                    amount=amount,
                )
                table_instance.save()

            # Process another model data (assuming it's similar to Table model fields)
            another_model_data = zip(
                request.POST.getlist('marka'),
                request.POST.getlist('transport'),
                request.POST.getlist('ref_no'),
                request.POST.getlist('lr_no'),
                request.POST.getlist('bill_no'),
                request.POST.getlist('packing'),
                request.POST.getlist('gst'),
                request.POST.getlist('tcs'),
                request.POST.getlist('tds'),
                request.POST.getlist('other'),
                request.POST.getlist('net_rtgs'),
                request.POST.getlist('net_diff'),
                request.POST.getlist('total')
            )
            for marka,transport,ref_no,lr_no,bill_no,packing,gst,tcs,tds,other,net_rtgs,net_diff,total in another_model_data:
                another_model_instance = JobRecDown(
                    purchaseup=purchase,  # Assuming AnotherModel has a ForeignKey to Sales
                    marka=marka,
                    transport=transport,
                    ref_no=ref_no,
                    lr_no=lr_no,
                    bill_no=bill_no,
                    packing=packing,
                    gst=gst,
                    tcs=tcs,
                    tds=tds,
                    other=other,
                    net_rtgs=net_rtgs,
                    net_diff=net_diff,
                    total=total,
                )
                another_model_instance.save()

            return redirect('index')  # Replace 'index' with your actual success URL
        else:
            # Form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = JobRecForm()

    accounts = Account.objects.all()
    account2 = Account.objects.filter(type='Purchase')
    items = Item.objects.all()

    return render(request, 'entry/job_rec.html', {'form': form, 'accounts': accounts, 'account2': account2, 'items': items})



def job_issue(request):
    if request.method == 'POST':
        form = JobIssForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.save()

            # Process table data
            table_data = zip(
                request.POST.getlist('sr'),
                request.POST.getlist('item_name'),
                request.POST.getlist('sizes'),
                request.POST.getlist('pcs'),
                request.POST.getlist('quantity'),
                request.POST.getlist('b_rate'),
                request.POST.getlist('rate'),
                request.POST.getlist('amount')
            )
            for sr, item_name, sizes, pcs, quantity, b_rate, rate, amount in table_data:
                table_instance = TableJobIss(
                    table_entry=purchase,
                    sr=sr,
                    item_name=item_name,
                    sizes=sizes,
                    pcs=pcs,
                    quantity=quantity,
                    b_rate=b_rate,
                    rate=rate,
                    amount=amount,
                )
                table_instance.save()

            # Process another model data (assuming it's similar to Table model fields)
            another_model_data = zip(
                request.POST.getlist('marka'),
                request.POST.getlist('transport'),
                request.POST.getlist('ref_no'),
                request.POST.getlist('lr_no'),
                request.POST.getlist('bill_no'),
                request.POST.getlist('packing'),
                request.POST.getlist('gst'),
                request.POST.getlist('tcs'),
                request.POST.getlist('tds'),
                request.POST.getlist('other'),
                request.POST.getlist('net_rtgs'),
                request.POST.getlist('net_diff'),
                request.POST.getlist('total')
            )
            for marka,transport,ref_no,lr_no,bill_no,packing,gst,tcs,tds,other,net_rtgs,net_diff,total in another_model_data:
                another_model_instance = JobIssDown(
                    purchaseup=purchase,  # Assuming AnotherModel has a ForeignKey to Sales
                    marka=marka,
                    transport=transport,
                    ref_no=ref_no,
                    lr_no=lr_no,
                    bill_no=bill_no,
                    packing=packing,
                    gst=gst,
                    tcs=tcs,
                    tds=tds,
                    other=other,
                    net_rtgs=net_rtgs,
                    net_diff=net_diff,
                    total=total,
                )
                another_model_instance.save()

            return redirect('index')  # Replace 'index' with your actual success URL
        else:
            # Form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = JobIssForm()

    accounts = Account.objects.all()
    account2 = Account.objects.filter(type='Sale')
    items = Item.objects.all()

    return render(request, 'entry/job_iss.html', {'form': form, 'accounts': accounts, 'account2': account2, 'items': items})
