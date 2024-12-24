from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.forms.models import inlineformset_factory
from .forms import *
from .master import *
from .models import *
from .entry import *
from .modify import *


from django.contrib import messages


def modify_cashentry(request):
    cashentries = Cashentry.objects.all()
    return render(request, 'modify/modify_cashentry.html', {'cashentries': cashentries})

def edit_cashentry(request, pk):
    cashentry = get_object_or_404(Cashentry, pk=pk)

    if request.method == 'POST':
        form = CashentryForm(request.POST, instance=cashentry)
        if form.is_valid():
            form.save()
            return redirect('modify_cashentry')  # Replace with your desired redirect URL after saving
    else:
        form = CashentryForm(instance=cashentry)

    return render(request, 'modify/edit_cashentry.html', {'form': form})


def delete_cashentry(request, pk):
    cashentry = get_object_or_404(Cashentry, pk=pk)
    
    if request.method == 'POST':
        cashentry.delete()
        return redirect('modify_cashentry')  # Redirect back to modify_cashentry URL
    
    return render(request, 'modify/delete_cashentry.html', {'cashentry': cashentry})





def modify_sales(request):
    sales_entries = SalesUp.objects.all()  # Fetch all SalesUp entries from the database

    return render(request, 'modify/modify_sales.html', {'sales_entries': sales_entries})



from django.forms import modelformset_factory
from django.forms.models import model_to_dict

def edit_sales(request, pk):
    salesup_instance = get_object_or_404(SalesUp, pk=pk)
    
    initial = model_to_dict(salesup_instance)
    
    TableFormSet = modelformset_factory(Table, form=TableForm, extra=1, can_delete=True)
    SalesDownFormSet = modelformset_factory(SalesDown, form=SalesDownForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        salesup_form = SalesUpForm(request.POST, instance=salesup_instance)
        table_formset = TableFormSet(request.POST, queryset=Table.objects.filter(table_entry=salesup_instance))
        salesdown_formset = SalesDownFormSet(request.POST, queryset=SalesDown.objects.filter(salesup=salesup_instance))
        
        if salesup_form.is_valid() and table_formset.is_valid() and salesdown_formset.is_valid():
            salesup_form.save()
            table_instances = table_formset.save(commit=False)
            for instance in table_instances:
                instance.table_entry = salesup_instance  # Ensure the field name matches your model
                instance.save()
            table_formset.save_m2m()

            salesdown_instances = salesdown_formset.save(commit=False)
            for instance in salesdown_instances:
                instance.salesup = salesup_instance
                instance.save()
            salesdown_formset.save_m2m()

            return redirect('modify_sales')  # Replace 'modify_sales' with your actual URL name
    
    else:
        salesup_form = SalesUpForm(instance=salesup_instance)
        table_formset = TableFormSet(queryset=Table.objects.filter(table_entry=salesup_instance))
        salesdown_formset = SalesDownFormSet(queryset=SalesDown.objects.filter(salesup=salesup_instance))
    
    return render(request, 'modify/edit_sales.html', {
        'salesup_form': salesup_form,
        'table_formset': table_formset,
        'salesdown_formset': salesdown_formset,
        'initial': initial,
    })



def delete_sales(request, pk):
    table_entry = get_object_or_404(Table, pk=pk)
    if request.method == 'POST':
        table_entry.delete()
        # Optionally, redirect to a success URL
        return redirect('modify_sales')  # Assuming 'modify_sales' is the URL name for your modify sales page
    # Handle GET requests if needed
    return redirect('modify_sales')  # Redirect to modify_sales page if not a POST request



def modify_jventry(request):
    entries = JVentry.objects.all()
    return render(request, 'modify/modify_jventry.html', {'entries': entries})

def edit_jventry(request, entry_id):
    entry = get_object_or_404(JVentry, pk=entry_id)
    if request.method == 'POST':
        form = JVentryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('modify_jventry')
    else:
        form = JVentryForm(instance=entry)
    return render(request, 'modify/edit_jventry.html', {'form': form})

def delete_jventry(request, entry_id):
    entry = get_object_or_404(JVentry, pk=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('modify_jventry')
    return render(request, 'modify/delete_jventry.html', {'entry': entry})





def modify_production(request):
    productions = Production.objects.all()
    return render(request, 'modify/modify_production.html', {'productions': productions})

def edit_production(request, production_id):
    production = get_object_or_404(Production, pk=production_id)
    if request.method == 'POST':
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            return redirect('modify_production')
    else:
        form = ProductionForm(instance=production)
    return render(request, 'modify/edit_production.html', {'form': form})

def delete_production(request, production_id):
    production = get_object_or_404(Production, pk=production_id)
    if request.method == 'POST':
        production.delete()
        return redirect('modify_production')
    return render(request, 'modify/delete_production.html', {'production': production})



def modify_saudapur(request):
    sauda_purchases = SaudaPur.objects.all()
    return render(request, 'modify/modify_saudapur.html', {'sauda_purchases': sauda_purchases})

def edit_saudapur(request, sauda_purchase_id):
    sauda_purchase = get_object_or_404(SaudaPur, pk=sauda_purchase_id)
    if request.method == 'POST':
        form = SaudaPurchase(request.POST, instance=sauda_purchase)
        if form.is_valid():
            form.save()
            return redirect('modify_saudapur')
    else:
        form = SaudaPurchase(instance=sauda_purchase)
    return render(request, 'modify/edit_saudapur.html', {'form': form})

def delete_saudapur(request, sauda_purchase_id):
    sauda_purchase = get_object_or_404(SaudaPur, pk=sauda_purchase_id)
    if request.method == 'POST':
        sauda_purchase.delete()
        return redirect('modify_saudapur')
    return render(request, 'modify/delete_saudapur.html', {'sauda_purchase': sauda_purchase})


def modify_saudasales(request):
    sauda_sales = SaudaSales.objects.all()
    return render(request, 'modify/modify_saudasales.html', {'sauda_sales': sauda_sales})

def edit_saudasales(request, sauda_sale_id):
    sauda_sale = get_object_or_404(SaudaSales, pk=sauda_sale_id)
    if request.method == 'POST':
        form = SaudaSalesForm(request.POST, instance=sauda_sale)
        if form.is_valid():
            form.save()
            return redirect('modify_saudasales')
    else:
        form = SaudaSalesForm(instance=sauda_sale)
    return render(request, 'modify/edit_saudasales.html', {'form': form})

def delete_saudasales(request, sauda_sale_id):
    sauda_sale = get_object_or_404(SaudaSales, pk=sauda_sale_id)
    if request.method == 'POST':
        sauda_sale.delete()
        return redirect('modify_saudasales')
    return render(request, 'modify/delete_saudasales.html', {'sauda_sale': sauda_sale})


def modifymain(request):
    # Fetch data from all three models
    jobissup_entries = JobIssUp.objects.all()
    table_jobiss_entries = TableJobIss.objects.all()
    jobissdown_entries = JobIssDown.objects.all()
    
    context = {
        'jobissup_entries': jobissup_entries,
        'table_jobiss_entries': table_jobiss_entries,
        'jobissdown_entries': jobissdown_entries,
    }
    return render(request, 'modify/modifymain.html', context)    

def modify_jobissue(request, jobissup_id):
    jobissup = get_object_or_404(JobIssUp, pk=jobissup_id)
    
    # Retrieve all related JobIssDown instances for jobissup
    jobissdown_instances = jobissup.jobissdown_set.all()
    
    if request.method == 'POST':
        # If POST request, process the forms
        jobiss_form = JobIssForm(request.POST, instance=jobissup)
        jobissdown_forms = [JobIssDownForm(request.POST, instance=jobissdown) for jobissdown in jobissdown_instances]
        
        if jobiss_form.is_valid() and all(jobissdown_form.is_valid() for jobissdown_form in jobissdown_forms):
            jobiss_form.save()
            for jobissdown_form in jobissdown_forms:
                jobissdown_form.save()
            return redirect('modify_jobissue', jobissup_id=jobissup.id)
    else:
        # If GET request, initialize forms with instances
        jobiss_form = JobIssForm(instance=jobissup)
        jobissdown_forms = [JobIssDownForm(instance=jobissdown) for jobissdown in jobissdown_instances]
    
    # Prepare context to render in template
    context = {
        'jobissup': jobissup,
        'jobiss_form': jobiss_form,
        'jobissdown_forms': jobissdown_forms,
    }
    
    return render(request, 'modify/modify_jobissue.html', context)


def edit_jobissue(request, jobissup_id, table_jobiss_id):
    table_jobiss = get_object_or_404(TableJobIss, pk=table_jobiss_id)
    
    if request.method == 'POST':
        form = TableJobIssForm(request.POST, instance=table_jobiss)
        if form.is_valid():
            form.save()
            return redirect('modify_jobissue', jobissup_id=jobissup_id)
    else:
        form = TableJobIssForm(instance=table_jobiss)
    
    context = {
        'form': form,
    }
    return render(request, 'modify/edit_jobissue.html', context)

def delete_jobissue(request, jobissup_id, table_jobiss_id):
    table_jobiss = get_object_or_404(TableJobIss, pk=table_jobiss_id)
    
    if request.method == 'POST':
        table_jobiss.delete()
        return redirect('modify_jobissue', jobissup_id=jobissup_id)
    
    context = {
        'table_jobiss': table_jobiss,
    }
    return render(request, 'modify/delete_jobissue.html', context)