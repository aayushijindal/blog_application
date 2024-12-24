from django import forms
from .models import *
from django.forms import modelformset_factory
from django.contrib.auth.models import User


class client_ForgotPassword_Form(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control',}))
    class Meta:
        model = User
        fields = ['email']

class client_OtpVerify_Form(forms.Form):
     otp = forms.CharField(required=True, error_messages={'required':'Please enter OTP'} ,max_length=6, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
     


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
       
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'



       
class CashentryForm(forms.ModelForm):
    class Meta:
        model = Cashentry
        fields = '__all__'



class Cashentryformmain(forms.ModelForm):
    class Meta:
        model = Cashentry
        fields = ['name', 'date', 'cl_balance', 'amount', 'rec_pay', 'remarks','round_date', 'kasar', 'round_cash', 'cash_dc', 'round_rtgs', 'rtgs_dc']   
        

class SaudaPurchase(forms.ModelForm):

    class Meta:
        model = SaudaPur
        fields = ['name', 'date', 'suda_no', 'item', 'quantity', 'rate', 'amount','bnd_kg', 'remarks']   

class SaudaSalesForm(forms.ModelForm):

    class Meta:
        model = SaudaSales
        fields = ['name', 'date', 'suda_no', 'item', 'quantity', 'rate', 'amount','bnd_kg', 'remarks']   


from django.forms.models import inlineformset_factory


class SalesUpForm(forms.ModelForm):
    class Meta:
        model = SalesUp
        fields = ['date_packing', 'esti_no', 'cr_days', 'party', 'book']

class SalesDownForm(forms.ModelForm):
    class Meta:
        model = SalesDown
        fields = ['marka', 'transport', 'ref_no', 'lr_no', 'bill_no', 'packing', 'gst', 'tcs', 'tds', 'other', 'net_rtgs', 'net_diff', 'total']

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['sr', 'item_name', 'sizes', 'pcs', 'quantity', 'b_rate', 'rate', 'amount']

TableFormSet = inlineformset_factory(
    SalesUp,         # Parent model
    Table,           # Child model
    form=TableForm,
    extra=1,         # Number of extra forms to display
    can_delete=True  # Allow deletion of existing records
)

SalesDownFormSet = inlineformset_factory(
    SalesUp,         # Parent model
    SalesDown,       # Child model
    form=SalesDownForm,
    extra=1,         # Number of extra forms to display
    can_delete=True  # Allow deletion of existing records
)





class PurchaseUpForm(forms.ModelForm):
    class Meta:
        model = PurchaseUp
        fields = ['date_packing', 'esti_no', 'cr_days', 'party', 'book']

class Table2Form(forms.ModelForm):
    class Meta:
        model = Tablenew
        fields = ['sr', 'item_name', 'sizes', 'pcs', 'quantity', 'b_rate', 'rate', 'amount']

class PurchaseDownForm(forms.ModelForm):
    class Meta:
        model = PurchaseDown
        fields = ['marka', 'transport', 'ref_no', 'lr_no', 'bill_no', 'packing', 'gst', 'tcs', 'tds', 'other', 'net_rtgs', 'net_diff', 'total']


class JVentryForm(forms.ModelForm):
    class Meta:
        model = JVentry
        fields = ['date', 'c_b', 'dr_name', 'cr_name', 'amount','remark']


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'


class JobRecForm(forms.ModelForm):
    class Meta:
        model = JobRecUp
        fields = ['date_packing', 'esti_no', 'cr_days', 'party', 'book']

class TableJobRecForm(forms.ModelForm):
    class Meta:
        model = TableJobRec
        fields = ['sr', 'item_name', 'sizes', 'pcs', 'quantity', 'b_rate', 'rate', 'amount']

class JobRecDownForm(forms.ModelForm):
    class Meta:
        model = JobRecDown
        fields = ['marka', 'transport', 'ref_no', 'lr_no', 'bill_no', 'packing', 'gst', 'tcs', 'tds', 'other', 'net_rtgs', 'net_diff', 'total']


class JobIssForm(forms.ModelForm):
    class Meta:
        model = JobIssUp
        fields = ['date_packing', 'esti_no', 'cr_days', 'party', 'book']

class TableJobIssForm(forms.ModelForm):
    class Meta:
        model = TableJobIss
        fields = ['sr', 'item_name', 'sizes', 'pcs', 'quantity', 'b_rate', 'rate', 'amount']

class JobIssDownForm(forms.ModelForm):
    class Meta:
        model = JobIssDown
        fields = ['marka', 'transport', 'ref_no', 'lr_no', 'bill_no', 'packing', 'gst', 'tcs', 'tds', 'other', 'net_rtgs', 'net_diff', 'total']
