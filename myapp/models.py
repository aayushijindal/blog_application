from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Homepage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=20, blank=True)
    organization_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    full_name = models.CharField(max_length=150, default='')  
    email = models.EmailField(max_length=254, unique=True)  # Ensure email field is unique

    # Add custom related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return self.username
    


class Account(models.Model):
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    person = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, blank=True, null=True)    
    type = models.CharField(max_length=100, blank=True, null=True)

    op_bal_cash = models.CharField(max_length=20, blank=True, null=True)
    op_cash_dc = models.CharField(max_length=100, blank=True, null=True)

    op_bal_rtgs = models.CharField(max_length=10, blank=True, null=True)
    op_rtgs_dc = models.CharField(max_length=100, blank=True, null=True)

    round_cash = models.CharField(max_length=20, blank=True, null=True)
    round_cash_dc = models.CharField(max_length=100, blank=True, null=True)

    round_rtgs = models.CharField(max_length=10, blank=True, null=True)
    round_rtgs_dc = models.CharField(max_length=100, blank=True, null=True)

    round_quantity = models.CharField(max_length=10, blank=True, null=True)
    r_date = models.CharField(max_length=100, blank=True, null=True)
    transport_name = models.CharField(max_length=100, blank=True, null=True)
    marka = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    anx_no = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    opening_stock = models.CharField(max_length=100, blank=True, null=True)
    pieces = models.CharField(max_length=100, blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    diff_rate_sale = models.CharField(max_length=100, blank=True, null=True)
    purchase = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

    
class SelectCash(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    
    @property
    def quality_no(self):
        return self.account.name


class Cashentry(models.Model):
    name = models.ForeignKey('Account', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)  # New field for date
    cl_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rec_pay = models.CharField(max_length=2, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    round_date = models.DateField(blank=True, null=True)  # New field for date
    kasar = models.CharField(max_length=100, blank=True, null=True)
    round_cash = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cash_dc = models.CharField(max_length=2, blank=True, null=True)
    round_rtgs = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rtgs_dc = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return str(self.name)  # Assuming self.name is the name field of the Account model

    class Meta:
        verbose_name_plural = 'Cash Entries'


class SaudaPur(models.Model):
    name = models.ForeignKey('Account', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)  # New field for date
    suda_no = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=2, blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=100,blank=True, null=True)  # New field for date
    bnd_kg = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Sauda Purchase'


class SaudaSales(models.Model):
    name = models.ForeignKey('Account', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)  # New field for date
    suda_no = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=2, blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=100,blank=True, null=True)  # New field for date
    bnd_kg = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Sauda Sales'




class SalesUp(models.Model):
    date_packing = models.DateField(blank=True, null=True)
    esti_no = models.CharField(max_length=100, blank=True, null=True)
    cr_days = models.CharField(max_length=100, blank=True, null=True)
    party = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='sales_up_party')
    book = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sales_up_book', limit_choices_to={'type': 'Sale'})

    def __str__(self):
        return f'SalesUp - {self.date_packing} - {self.esti_no} - {self.cr_days} - {self.party} - {self.book}'

    class Meta:
        verbose_name_plural = 'Sales'


class Table(models.Model):
    table_entry = models.ForeignKey(SalesUp, on_delete=models.CASCADE, related_name='tables')
    sr = models.CharField(max_length=200, blank=True, null=True)
    item_name = models.CharField(max_length=20, blank=True, null=True)
    sizes = models.CharField(max_length=200, blank=True, null=True)
    pcs = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    b_rate = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'Table - {self.item_name}'


class SalesDown(models.Model):
    salesup = models.ForeignKey(SalesUp, on_delete=models.CASCADE, related_name='sales_downs')
    marka = models.CharField(max_length=100, blank=True, null=True)
    transport = models.CharField(max_length=20, blank=True, null=True)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    lr_no = models.CharField(max_length=100, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    gst = models.CharField(max_length=100, blank=True, null=True)
    tcs = models.CharField(max_length=20, blank=True, null=True)
    tds = models.CharField(max_length=20, blank=True, null=True)
    other = models.CharField(max_length=100, blank=True, null=True)
    net_rtgs = models.CharField(max_length=20, blank=True, null=True)
    net_diff = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'SalesDown - {self.marka}'

    




class PurchaseUp(models.Model):
    date_packing = models.DateField(blank=True, null=True)
    esti_no = models.CharField(max_length=100,blank=True, null=True)
    cr_days = models.CharField(max_length=100,blank=True, null=True)
    party = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='party1')
    book = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='book1', limit_choices_to={'type': 'Purchase'})

    def __str__(self):
        return f'{self.date_packing} - {self.esti_no} ({self.cr_days}, {self.party}, {self.book})'
    
    class Meta:
        verbose_name_plural = 'Purchase'

class Tablenew(models.Model):
    table_entry = models.ForeignKey(PurchaseUp, on_delete=models.CASCADE, related_name='purchase_table')
    sr = models.CharField(max_length=200, blank=True, null=True)
    item_name = models.CharField(max_length=20, blank=True, null=True)
    sizes = models.CharField(max_length=200, blank=True, null=True)
    pcs = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    b_rate = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.item_name}'

class PurchaseDown(models.Model):
    purchaseup = models.ForeignKey(PurchaseUp, on_delete=models.CASCADE)
    marka = models.CharField(max_length=100, blank=True, null=True)
    transport = models.CharField(max_length=20, blank=True, null=True)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    lr_no = models.CharField(max_length=100, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    gst = models.CharField(max_length=100, blank=True, null=True)
    tcs = models.CharField(max_length=20, blank=True, null=True)
    tds = models.CharField(max_length=20, blank=True, null=True)
    other = models.CharField(max_length=100, blank=True, null=True)
    net_rtgs = models.CharField(max_length=20, blank=True, null=True)
    net_diff = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return f'{self.marka}'
    
class JVentry(models.Model):
    date = models.DateField(blank=True, null=True)
    c_b = models.CharField(max_length=100, blank=True, null=True)
    dr_name = models.ForeignKey('Account', blank=True, null=True, on_delete=models.CASCADE, related_name='Dr_name')
    cr_name = models.ForeignKey('Account', blank=True, null=True, on_delete=models.CASCADE, related_name='Cr_name')
    amount = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.date}'
    

class Production(models.Model):
    date = models.DateField(blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    issue_to = models.ForeignKey('Account', blank=True, null=True, on_delete=models.CASCADE, related_name='Issue_to')
    item = models.ForeignKey('Item', blank=True, null=True, on_delete=models.CASCADE, related_name='Item')
    quantity = models.CharField(max_length=100, blank=True, null=True)
    pieces = models.CharField(max_length=20, blank=True, null=True)
    rec_iss = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.date}'
    


class JobRecUp(models.Model):
    date_packing = models.DateField(blank=True, null=True)
    esti_no = models.CharField(max_length=100,blank=True, null=True)
    cr_days = models.CharField(max_length=100,blank=True, null=True)
    party = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='partyjobrec')
    book = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='bookjobrec', limit_choices_to={'type': 'Purchase'})

    def __str__(self):
        return f'{self.date_packing} - {self.esti_no} ({self.cr_days}, {self.party}, {self.book})'
    
    class Meta:
        verbose_name_plural = 'Job Receipt'

class TableJobRec(models.Model):
    table_entry = models.ForeignKey(JobRecUp, on_delete=models.CASCADE, related_name='jobrec_table')
    sr = models.CharField(max_length=200, blank=True, null=True)
    item_name = models.CharField(max_length=20, blank=True, null=True)
    sizes = models.CharField(max_length=200, blank=True, null=True)
    pcs = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    b_rate = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.item_name}'

class JobRecDown(models.Model):
    purchaseup = models.ForeignKey(JobRecUp, on_delete=models.CASCADE)
    marka = models.CharField(max_length=100, blank=True, null=True)
    transport = models.CharField(max_length=20, blank=True, null=True)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    lr_no = models.CharField(max_length=100, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    gst = models.CharField(max_length=100, blank=True, null=True)
    tcs = models.CharField(max_length=20, blank=True, null=True)
    tds = models.CharField(max_length=20, blank=True, null=True)
    other = models.CharField(max_length=100, blank=True, null=True)
    net_rtgs = models.CharField(max_length=20, blank=True, null=True)
    net_diff = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return f'{self.marka}'
    

class JobIssUp(models.Model):
    date_packing = models.DateField(blank=True, null=True)
    esti_no = models.CharField(max_length=100, blank=True, null=True)
    cr_days = models.CharField(max_length=100, blank=True, null=True)
    party = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='partyjobiss')
    book = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='bookjobiss', limit_choices_to={'type': 'Sale'})

    def __str__(self):
        return f'{self.date_packing} - {self.esti_no} ({self.cr_days}, {self.party}, {self.book})'
    
    class Meta:
        verbose_name_plural = 'Job Issue'

class TableJobIss(models.Model):
    table_entry = models.ForeignKey(JobIssUp, on_delete=models.CASCADE, related_name='jobiss_table')
    sr = models.CharField(max_length=200, blank=True, null=True)
    item_name = models.CharField(max_length=20, blank=True, null=True)
    sizes = models.CharField(max_length=200, blank=True, null=True)
    pcs = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    b_rate = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.item_name}'

class JobIssDown(models.Model):
    jobiss_up = models.ForeignKey(JobIssUp, on_delete=models.CASCADE, related_name='jobissdown')
    marka = models.CharField(max_length=100, blank=True, null=True)
    transport = models.CharField(max_length=20, blank=True, null=True)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    lr_no = models.CharField(max_length=100, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    gst = models.CharField(max_length=100, blank=True, null=True)
    tcs = models.CharField(max_length=20, blank=True, null=True)
    tds = models.CharField(max_length=20, blank=True, null=True)
    other = models.CharField(max_length=100, blank=True, null=True)
    net_rtgs = models.CharField(max_length=20, blank=True, null=True)
    net_diff = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=False, null=True)

    def __str__(self):
        return f'{self.marka}'
