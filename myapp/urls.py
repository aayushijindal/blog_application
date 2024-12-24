from django.urls import path
from . import views,client,master,entry,modify,report,summary,tools
from .views import index
from .client import *
from .master import *
from .modify import *
from .report import *
from .summary import *
from .tools import *


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.main, name='main'),
    path('register/', client.register, name='register'),
    path('login/', client.login_view, name='login'),
    path('forgot_password/', client.client_ForgotPassword, name='forgot_password'),
    path('verify_otp/', client.client_OtpVerify, name='verify_otp'),
    path('reset_password/', client.client_ResetPassword, name='reset_password'),
    path('logout_view/',client.logout_view, name = 'logout_view'),

    
    path('accounts/', master.accounts, name='accounts'),
    path('groups/', master.groups, name='groups'),
    path('items/', master.items, name='items'),


    path('cash_entry/', entry.cash_entry, name='cash_entry'),
    path('sales/', entry.sales, name='sales'),
    path('purchase/', entry.purchase, name='purchase'),
    path('cashentryform/', entry.cashentryform, name='cashentryform'),
    path('sauda_purchase/', entry.sauda_purchase, name='sauda_purchase'),
    path('sauda_sales/', entry.sauda_sales, name='sauda_sales'),
    path('jventry/', entry.jventry, name='jventry'),
    path('production/', entry.production, name='production'),
    path('job_rec/', entry.job_rec, name='job_rec'),
    path('job_issue/', entry.job_issue, name='job_issue'),



    path('modify_cashentry/', modify.modify_cashentry, name='modify_cashentry'),
    path('edit_cashentry/<int:pk>/', modify.edit_cashentry, name='edit_cashentry'),
    path('delete_cashentry/<int:pk>/', modify.delete_cashentry, name='delete_cashentry'),
    path('modify_sales/', modify.modify_sales, name='modify_sales'),
    path('edit_sales/<int:pk>/', modify.edit_sales, name='edit_sales'),
    path('delete_sales/<int:pk>/', modify.delete_sales, name='delete_sales'),
    path('modify_jventry', modify.modify_jventry, name='modify_jventry'),
    path('edit_jventry/<int:entry_id>/', modify.edit_jventry, name='edit_jventry'),
    path('delete_jventry/<int:entry_id>/', modify.delete_jventry, name='delete_jventry'),
    path('modify_production/', modify.modify_production, name='modify_production'),
    path('edit_production/<int:production_id>/', modify.edit_production, name='edit_production'),
    path('delete_production/<int:production_id>/', modify.delete_production, name='delete_production'),
    path('modify_saudapur/', modify.modify_saudapur, name='modify_saudapur'),
    path('edit_saudapur/<int:sauda_purchase_id>/', modify.edit_saudapur, name='edit_saudapur'),
    path('delete_saudapur/<int:sauda_purchase_id>/', modify.delete_saudapur, name='delete_saudapur'),
    path('modify_saudasales/', modify.modify_saudasales, name='modify_saudasales'),
    path('edit_saudasales/<int:sauda_sale_id>/', modify.edit_saudasales, name='edit_saudasales'),
    path('delete_saudasales/<int:sauda_sale_id>/', modify.delete_saudasales, name='delete_saudasales'),
    path('modifymain/', modify.modifymain, name='modifymain'),
    path('modify_jobissue/<int:jobissup_id>/', modify.modify_jobissue, name='modify_jobissue'),
    path('edit_jobissue/<int:jobissup_id>/<int:table_jobiss_id>/', modify.edit_jobissue, name='edit_jobissue'),
    path('delete_jobissue/<int:jobissup_id>/<int:table_jobiss_id>/', modify.delete_jobissue, name='delete_jobissue'),



    path('packing_book/', report.packing_book, name='packing_book'),
    path('stock_book/', report.stock_book, name='stock_book'),
    path('dispatch_book/', report.dispatch_book, name='dispatch_book'),
    path('size_book/', report.size_book, name='size_book'),
    path('stock_summary/', report.stock_summary, name='stock_summary'),
    path('lot_summary/', report.lot_summary, name='lot_summary'),
    path('production_register/', report.production_register, name='production_register'),
    path('lot_register/', report.lot_register, name='lot_register'),


    path('dispatch_summary/', summary.dispatch_summary, name='dispatch_summary'),
    path('customer_report/', summary.customer_report, name='customer_report'),
    path('transport_report/', summary.transport_report, name='transport_report'),


    path('packing_slip/', tools.packing_slip, name='packing_slip'),
    path('packing_slip_new/', tools.packing_slip_new, name='packing_slip_new'),
    path('remove_data/', tools.remove_data, name='remove_data'),

]
