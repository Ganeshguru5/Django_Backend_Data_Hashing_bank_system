from distutils.sysconfig import customize_compiler
from os import link
from django.forms.forms import Form
from django.http import request, response
from django.shortcuts import  redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import OBLoginform, savingsLoginform,ATMLoginform,Customerform
from django.contrib import auth
from .models import savingsLogin,OBLogin,ATMLogin,Customer_details,linkedAccounts,transactionHistory
import random
from twilio.rest import Client



# Create your views here.
def homepage(request):
    return render (request , 'index.html')

def login(request):
    return render (request,'login.html')

def savingsloginform(request):
    form=savingsLoginform()
    return render (request,'Savings_login.html',{'form':form})

def ATMloginform(request):
    form=ATMLoginform()
    return render (request,'ATM_login.html',{'form':form})

def OBloginform(request):
    form=OBLoginform
    return render (request,'OB_login.html',{'form':form})

def registerOB(request):
    return render(request,'RegisterOB.html')

mobnum=''
nameonpassbook=''
birthdate=''
accnumber=''
atmnum=''
otp=''
transotp=''
loginname=''
id=0
def ATMlogin(request):
    global loginname
    loginname=='ATM_login'
    
    if request.method == 'POST':
       ATMnumber1=request.POST['ATMnumber']
       mobnum1=request.POST['mobnum']
       global mobnum
       global atmnum
       atmnum=ATMnumber1
       mobnum=mobnum1
       user_set=Customer_details.objects.all()
       for user in user_set.iterator():
            if (user.ATMnumber==atmnum):
                id=user.id
            
       if Customer_details.objects.filter(ATMnumber=ATMnumber1).exists() and Customer_details.objects.filter(mobnum=mobnum1).exists() :
                current_user={"id":id}
                current_user=Customer_details.objects.get(id=id)
                print(current_user)
                return render (request,'Verify.html',{'current_user':current_user})
    # people = Customer_details.objects.raw('SELECT username FROM app_customer_details WHERE username=Bhavani')
    # print(people,"tis is ")
    form=ATMLoginform()
    return render (request,'ATM_login.html',{'form':form})

def savingslogin(request):
    
    if request.method == 'POST':
       nameonpassbook1=request.POST['nameonpassbook']
       birthdate1=request.POST['birthdate']
       accnumber1=request.POST['accnumber']
       mobnum1=request.POST['mobnumber']
       global nameonpassbook
       global birthdate
       global accnumber
       global mobnum
       nameonpassbook=nameonpassbook1
       birthdate=birthdate1
       accnumber=accnumber1
       mobnum=mobnum1
       user_set=Customer_details.objects.all()
       for user in user_set.iterator():
            if (user.accnumber==accnumber):
                id=user.id
            
       if Customer_details.objects.filter(nameonpassbook=nameonpassbook).exists() and Customer_details.objects.filter(birthdate=birthdate).exists() and Customer_details.objects.filter(accnumber=accnumber).exists() and Customer_details.objects.filter(mobnum=mobnum).exists() :
                current_user={"id":id}
                current_user=Customer_details.objects.get(id=id)
                return render (request,'Verify.html',{'current_user':current_user})

    form=ATMLoginform()
    return render (request,'ATM_login.html',{'form':form})

def sendsms(request):
    username=''
    ATMnumber=''
    rannum=random.randrange(1000, 9999)
    global otp
    otp=str(rannum)
    
    number=str(mobnum)
    form=Customerform()
    print(otp)
    if number!='':
       """  if otp:
            account_sid = 'ACbf2bf8c5cff79340cb3998d25d812fe1'
            auth_token = '5a5416d7e0e7bd4b7e25aaefca94326f'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                    body='Your otp is '+otp,
                                    from_='+15076462191',
                                    to='+91'+number
                                    )

            print(message.body) """
        
    else:
        return redirect('/'+loginname)
    if request.method == 'POST':
        username=request.POST['username']
        ATMnumber=request.POST['ATMnumber']
        user_set=Customer_details.objects.all()
        for user in user_set.iterator():
            if (user.ATMnumber==ATMnumber):
                id=user.id
        if Customer_details.objects.filter(username=username).exists() and Customer_details.objects.filter(ATMnumber=ATMnumber).exists() :
            current_user={"id":id}
            current_user=Customer_details.objects.get(id=id)
    
            return render (request,'Otp.html',{'current_user':current_user})
    

def verifiedDashboard(request):
    
    otpin=request.POST['otp']
    username=request.POST['username']
    ATMnumber=request.POST['ATMnumber']
    user_set=Customer_details.objects.all()
    
    for user in user_set.iterator():
        if (user.ATMnumber==ATMnumber):
            id=user.id
    if Customer_details.objects.filter(username=username).exists() and Customer_details.objects.filter(ATMnumber=ATMnumber).exists() and otpin==otp :
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        linked = linkedAccounts.objects.all().filter(accnumber=current_user.accnumber)
        history = transactionHistory.objects.all().filter(accnumber=current_user.accnumber)

        return render (request,'Dashboard.html',{'current_user':current_user , 'linked':linked,'history':history})
    current_user={"id":id}
    current_user=Customer_details.objects.get(id=id)
    
    
    return render(request,'Dashboard.html',{'current_user':current_user})


def Logout(request):
    return render (request,'index.html')

def balance(request):
    print(atmnum)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        print(user.accnumber,"@@@")
        if (user.ATMnumber==atmnum):
            id=user.id
    
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        linked = linkedAccounts.objects.all().filter(accnumber=current_user.accnumber)
        history = transactionHistory.objects.all().filter(accnumber=current_user.accnumber)
        
        return render (request,'balance.html',{'current_user':current_user , 'linked':linked,'history':history})
    
    #current_user={"id":id}
    
def insurance(request):
    print(atmnum)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        return render (request,'insurance.html',{'current_user':current_user})
    #current_user={"id":id}
    current_user=Customer_details.objects.get(id=id) 
    return render (request,'insurance.html',{'current_user':current_user})
           
def bookandorder(request):
    print(atmnum)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        return render (request,'book_n_order.html',{'current_user':current_user})
    #current_user={"id":id}
    current_user=Customer_details.objects.get(id=id) 
    return render (request,'book_n_order.html',{'current_user':current_user})

def shoping(request):
    print(atmnum)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        return render (request,'shop.html',{'current_user':current_user})
    #current_user={"id":id}
    current_user=Customer_details.objects.get(id=id) 
    return render (request,'shop.html',{'current_user':current_user})

def homeback(request):
    print(atmnum)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        return render (request,'Dashboard.html',{'current_user':current_user})
    #current_user={"id":id}
    current_user=Customer_details.objects.get(id=id) 
    return render (request,'Dashboard.html',{'current_user':current_user})

def sentmoney(request):
    print(atmnum)

    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
    print(current_user.password)
    if current_user.ob_registered==False:
        return render(request,'404_OB.html',{'current_user':current_user})
    elif current_user.ob_registered==True:
        return render(request,'moneysent_ver.html',{'current_user':current_user})
#ATMnumber
def obverified(request):
    print(atmnum)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        return render(request,'transactionpage.html',{'current_user':current_user})
 



def transfercash(request):
    accnumber=request.POST['accnumber']
    currentacc = request.POST.get("current_account")
    amount=int(request.POST['amount'])
    pin=request.POST['pin']
    transactionType = request.POST.get("transactiontype")
    fees = request.POST.get("fee")
    date = request.POST.get("date")


    amountstr=str(amount)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
    
    for user2 in user_set.iterator():
        if (user2.accnumber==accnumber):
            id1=user2.id
            second_user=Customer_details.objects.get(id=id1)
    
    if (current_user.pin == pin):
        final_amount=int(second_user.accountbalance)+amount
        final_amount1=str(final_amount)
        print(type(final_amount1))
        mybalnce=int(current_user.accountbalance)-amount
        mybalnce1=str(mybalnce)
        transacHis = transactionHistory()
        transacHis.amounttransfered =amount 
        transacHis.accnumber = currentacc  
        transacHis.second_acc = accnumber 
        transacHis.transactiontype = transactionType
        transacHis.fees = fees
        transacHis.Date = date
        transacHis.save()
    #second_user=Customer_details.objects.raw("UPDATE app_customer_details set accountbalance="+final_amount1+" WHERE accnumber="+accnumber)
        Customer_details.objects.filter(accnumber=accnumber).update(accountbalance=final_amount1)
        Customer_details.objects.filter(ATMnumber=atmnum).update(accountbalance=mybalnce1)

    

        """ account_sid = 'ACbf2bf8c5cff79340cb3998d25d812fe1'
        auth_token = '5a5416d7e0e7bd4b7e25aaefca94326f'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                            body='Cash amount '+amountstr+ 'sent successfully',
                            from_='+15076462191',
                            to='+91'+current_user.mobnum
                            )

        print(message.body)
        account_sid = 'AC9b48060f616e7a945332f792c8c22730'
        auth_token = 'f0883c5fbc5f5ed5ad120be42e2f5436'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                            body='You received Rs.'+amountstr+" from "+current_user.username,
                            from_='+15038226689',
                            to='+91'+second_user.mobnum
                            )

        print(message.body) """
        return render (request,'sucesstrans.html',{'current_user':current_user,'second_user':second_user})

def linkaccpage(request):
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        return render(request,'linkaccount.html',{'current_user':current_user})
    

def linkaccount(request):
    current_user = Customer_details.objects.all().filter(ATMnumber = atmnum)
    linkacc = linkedAccounts()
    linkacc.country=request.POST.get('country')
    linkacc.accounttype=request.POST.get('accounttype')
    linkacc.accnumber =request.POST.get('accnumber')
    linkacc.bank_name=request.POST.get('bank_name')
    linkacc.bank_branch_code=request.POST.get('branch_code')
    linkacc.bank_ifsc_code=request.POST.get('bank_code')
    linkacc.linkedaccnumber=request.POST.get('linkaccnumber')
    linkacc.bank_location=request.POST.get('bank_location')

    if(Customer_details.objects.all().filter(accnumber = request.POST.get('accnumber')).exists()):
        linkacc.save()
        print("account linked successfully")
        
    else:
        print("account not linked")
    
    
    return redirect('/linkaccpage',{"current_user":current_user})
    #return render(request,'balance.html',{"current_user":current_user})  

def transfertobank(request):
    amount = request.POST.get('amount')
    accnumber = request.POST.get("linkedaccnum")
    currentacc = request.POST.get("accnumber")
    transactionType = request.POST.get("transactiontype")
    fees = request.POST.get("fee")
    date = request.POST.get("date")


    print(currentacc,',',transactionType,',',fees,',',date)

    transacHis = transactionHistory()
    transacHis.amounttransfered =amount
    transacHis.accnumber = currentacc
    transacHis.second_acc = accnumber
    transacHis.transactiontype = transactionType
    transacHis.fees = fees
    transacHis.Date = date

    print(amount , "amount")
    print(accnumber , "accnumber")
    accnumber=request.POST['linkedaccnum']
    amount=int(request.POST['amount'])
    amountstr=str(amount)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
    
    for user2 in user_set.iterator():
        if (user2.accnumber==accnumber):
            id1=user2.id
            second_user=Customer_details.objects.get(id=id1)
    
    final_amount=int(second_user.accountbalance)+amount
    final_amount1=str(final_amount)
    print(type(final_amount1))
    mybalnce=int(current_user.accountbalance)-(amount+30)
    mybalnce1=str(mybalnce)
    #second_user=Customer_details.objects.raw("UPDATE app_customer_details set accountbalance="+final_amount1+" WHERE accnumber="+accnumber)
    Customer_details.objects.filter(accnumber=accnumber).update(accountbalance=final_amount1)
    Customer_details.objects.filter(ATMnumber=atmnum).update(accountbalance=mybalnce1)
    transacHis.save()
    return redirect('/Balance-Amount')

def withdrawpage(request):
    linkedacc=request.POST.get('linker')
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
        return render(request,'withdraw.html',{'current_user':current_user})


def withdraw(request):
    amount = request.POST.get('amount')
    accnumber = request.POST.get("linkedaccnum")
    currentacc = request.POST.get("accnumber")
    transactionType = request.POST.get("transactiontype")
    fees = request.POST.get("fee")
    date = request.POST.get("date")

    transacHis = transactionHistory()
    transacHis.amounttransfered =amount
    transacHis.accnumber = currentacc
    transacHis.second_acc = accnumber
    transacHis.transactiontype = transactionType
    transacHis.fees = fees
    transacHis.Date = date

    print(currentacc,',',transactionType,',',fees,',',date)
    print(amount , "amount")
    print(accnumber , "accnumber")
    accnumber=request.POST['linkedaccnum']
    amount=int(request.POST['amount'])
    amountstr=str(amount)
    user_set=Customer_details.objects.all()
    for user in user_set.iterator():
        if (user.ATMnumber==atmnum):
            id=user.id
    if Customer_details.objects.filter(ATMnumber=atmnum).exists():
        current_user={"id":id}
        current_user=Customer_details.objects.get(id=id)
    
    for user2 in user_set.iterator():
        if (user2.accnumber==accnumber):
            id1=user2.id
            second_user=Customer_details.objects.get(id=id1)

    final_amount=int(second_user.accountbalance)-amount
    final_amount1=str(final_amount)
    print(type(final_amount1))
    mybalnce=int(current_user.accountbalance)+(amount)
    mybalnce1=str(mybalnce)
    #second_user=Customer_details.objects.raw("UPDATE app_customer_details set accountbalance="+final_amount1+" WHERE accnumber="+accnumber)
    Customer_details.objects.filter(accnumber=accnumber).update(accountbalance=final_amount1)
    Customer_details.objects.filter(ATMnumber=atmnum).update(accountbalance=mybalnce1)
    transacHis.save()
    return redirect('/Balance-Amount')
