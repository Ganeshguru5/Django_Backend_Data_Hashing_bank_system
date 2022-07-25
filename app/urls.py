from unicodedata import name
from django.urls import path
from six import viewvalues
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('loginpage',views.login,name='login_option'),
    path('savings_login',views.savingsloginform,name='Savings_Login'),
    path('ATM_login',views.ATMloginform,name='ATM_Login'),
    path('OB_login',views.OBloginform,name='OB_Login'),
    path('Register_OB',views.registerOB,name='Register_OB'),
    path('dashboardATM',views.ATMlogin,name='dashboardATM'),
    path('dashboardsavings',views.savingslogin,name='dashboardSavings'),
    path('sentsms',views.sendsms,name='sms_sent'),
    path('VerifiedDashboard',views.verifiedDashboard,name='Dashboard'),
    path('Balance-Amount',views.balance,name='balanceamount'),
    path('Logout',views.Logout,name='Logout'),
    path('getinsurance',views.insurance,name='Insurance'),
    path('booknorder',views.bookandorder,name='booknorder'),
    path('shoping',views.shoping,name='shopping'),
    path('homeback',views.homeback,name='backDashboard'),
    path('sentmoney',views.sentmoney,name='Sentmoney'),
    path('obverified',views.obverified,name='OBverified'),
    path('transfercash',views.transfercash,name='transfercash'),
    path('linkaccount',views.linkaccount,name='linkaccount'),
    path('transfertobank',views.transfertobank,name="transfertobank"),
    path('withdrawpage',views.withdrawpage,name="withdrawpage"),
    path('linkaccpage',views.linkaccpage,name='linkaccpage')
    
]


    

