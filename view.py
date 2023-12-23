from django.shortcuts import render
from sai.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django .http import HttpResponse


def homepage (request):
    return render(request,'welcome.html')

def localvariable(request):
    my_variable = "Hello World"
    return render(request, 'local1.html', {'my_variable':my_variable})



def globalvariable(request):
    return render(request, 'global1.html', {'my_variable':"welcome"})
def getandpost(request):
    return render(request, 'get and post.html')

def add(request):
    if request.method=='POST':
        num1=int(request.POST.get('num1'))
        num2=int(request.POST.get('num2'))
        result=num1+num2
        return render(request,'result.html',{'result':result})
    return render(request, 'add.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'password':
            return render(request,'success.html',{'username': username})
        else:
            error ='invalid username or password please try again'
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')

def grade_form(request):
    if request.method=='POST':
        name = request.POST.get('name')
        marks1=int( request.POST.get('marks1'))
        marks2=int( request.POST.get('marks2'))
        marks3=int( request.POST.get('marks3'))
        total=marks1+marks2+marks3
        avg=(marks1+marks2+marks3)/2
        if(avg >=90 and avg <=100):
           grade='A GRADE'
        else:
           grade='failure'
        return render(request,'result1.html',{'name':name,'total':total,'avg':avg,'grade':grade})
    return render(request,'grade1.html')

def sai(request):
    return render(request,'welcome2.html')


def localvariable(request):
    #s='sai siva sankar' local variables
    return render (request,'local1.html',{'variable':'hello django students'})

def gp(request):
    return render(request, 'get and post.html')

def add(request):
    if request.method=='POST':
        a=int(request.POST.get('a'))
        b=int(request.POST.get('b'))
        result=a+b
        return render(request,'result.html',{'result':result})
    return render(request,'add1.html')

def login1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username =='admin' and password =='password':
            return render (request,'success.html',{'username':username})
        else:
            error ='invalid username or password please try again'
            return render(request,'success.html',{'error':error})
    else:
        return render(request,'login1.html')

    
def page2(request):
    return render(request,'page2.html')

def page4(request):
    return render(request,'page4.html')
    


def display(request):
    return render (request,'welcome.html')

def value(request):
    if request.method=="POST":       
        a= request.POST.get('name')
        b= request.POST.get('email')
        c= request.POST.get('phone')
        en=Enquiry(name=a,email=b,phone=c)
        en.save()
    return render(request,"login2.html")


def student_result(request):
    students=[
        {'name':'vikas','maths':90,'science':85,'english':95},
        {'name':'vikas','maths':90,'science':85,'english':95},
        {'name':'vikas','maths':90,'science':85,'english':95},
        {'name':'vikas','maths':90,'science':85,'english':95}
    ]
    return render(request,'result2.html',{'students':students})

def even(request):
    numbers=[i for i in range(1,11) if i%2==0]
    return render(request,'even.html',{'numbers':numbers})


def grade(request):
    if request.method == 'POST':     
          name=request.POST.get('name')
          marks1=int(request.POST.get('marks1'))
          marks2=int(request.POST.get('marks2'))
          marks3=int(request.POST.get('marks3'))
          total=marks1+marks2+marks3
          avg=total/3
          if(avg>=95 and avg <=100):
            grade='HD'
          elif avg>=75 and avg<=94:
            grade='D'
          elif avg>=65 and avg<=74:
            grade='c'
          elif avg>=50 and avg<=64:
            grade='pass'
          elif avg>=0 and avg<=49:
            grade='fail'
          else:
            grade='invalid'
          
        
        
          
     
          return render(request, 'result3.html', {'name': name, 'total': total, 'avg': avg, 'grade': grade})
    else:
      
        return render(request, 'eliif.html')


def big(request):
    if request.method == 'POST':     
       
          Num1=int(request.POST.get('Num1'))
          Num2=int(request.POST.get('Num2'))
          Num3=int(request.POST.get('Num3'))
        
          if(Num1>Num2 and Num1> Num3):
            result='Num1 is big'
          elif Num2>Num1 and Num2> Num3:
            result='Num2 is big'
          elif Num3>Num1 and Num3>Num2:
            result='Num3 is big'
          else:
            result='all values are equal'

          return render(request, 'result4.html', { 'result': result})
    else:
      
        return render(request, 'task1(big3 num).html')



def posstive(request):
    if request.method == 'POST':
        Num1=int(request.POST.get('Num1'))
        if Num1>0:
            result='posstive num'
        elif Num1<0:
            result='Negative number'
        else:
            result='zero'
        
          

        return render(request, 'result4.html', { 'result': result})
    else:
      
        return render(request, 'task1(pass num).html')


def simple(request):
    if request.method == 'POST':
        N1=int(request.POST.get('N1'))
        N2=int(request.POST.get('N2'))    
       
        operator=request.POST['operator']
        if operator=='add':
            result=N1+N2
        elif operator=='sub':
            result=N1-N2
        elif operator=='mul':
            result=N1*N2
        elif  operator=='div':
            if  N2!=0:
                result=N1/N2
            else:
                result='sai'
        
          

        return render(request, 'result4.html', { 'result': result})
    else:
      
        return render(request, 'task1(simple num).html')

def table(request):
    return render(request,'table.html')


def atm(request):
    balance = 1000
    if request.method == 'POST':
     transaction_type=request.POST.get('transaction_type')   #withdraw
     amount=int(request.POST.get('amount')) #233
     if transaction_type=='check_balance':
      message=balance
     elif transaction_type=='deposit':
          message=amount+balance# 1500+1000=2500
     elif transaction_type=='withdraw':
        if amount%100==0:
          if amount>balance:
           message="overdraft"
          else:
           message=balance-amount # 1000-600 =400
        else:
         message="multiple of 100"
     
     return render(request, 'succ.html', {'message': message})
    else:

     return render(request, 'atm.html')



def sweep(request):
    if request.method=='POST':
        a=int(request.POST.get('a'))
        b=int(request.POST.get('b'))
        result=a
        a=b
        b=result
        return render(request,'sweep(res).html',{'a':a,'b':b})
    else:
        return render(request,'sweep.html')


def lcm(request):
    contex={}
    if request.method=='POST':
        num1=int(request.POST.get('num1'))
        num2=int(request.POST.get('num2'))
        result=cal_lcm(num1,num2)
        contex['result']=result
    return render(request,'lcm.html',contex)
def cal_lcm(a,b):
    mul=max(a,b)
    while True:
        if mul%a==0 and mul%b==0:
            return mul
        mul+=1



def perfect(request):
    context = {}
    if request.method == 'POST':
        number = int(request.POST.get('number'))#6
        is_perfect = check_perfect(number)#6
        context['number'] = number#6
        context['is_perfect'] = is_perfect #6
    return render(request, 'perfect.html', context)
def check_perfect(number):#6
    divisor_sum = 0
    for i in range(1, number):# 6<6
        if number % i == 0:# 6%5==0
            divisor_sum += i#0+1=1+2=3+3=6
         
    return divisor_sum == number # 6==6



def gcd(request):
    contex={}
    if request.method=='POST':
        num1=int(request.POST.get('num1'))# 3
        num2=int(request.POST.get('num2'))# 2
        result=cal_gcd(num1,num2) #1
        contex['result']=result
    return render(request,'gcd.html',contex)
def cal_gcd(a,b):# 3,2  # 2,1  1,0
    if b==0: # 2==0:f 1==0 F 0==0 t
        return a #1
    else:#  
        return cal_gcd(b,a%b)  # 2,3%2=1 # 1, 2%1=0



def vowelcount(request):
    context={}
    if request.method=='POST':
        text=request.POST.get('text')
        vowel_count=count_vowel(text)
        context['vowel_count']=vowel_count
    return render(request,'vowelcount.html',context)

def count_vowel(text):
    vowels='AEIOUaeiou'
    vowel=''
    c=0
    for char in text:
        if char in vowels:# if char not in vowels:
            vowel+=char
            c=c+1
    return vowel,c


def fact(request):
    if request.method=='POST':
        num=int(request.POST.get('number'))
        def cf(n):
            if n==0:
                return 1
            else:
                return n*cf(n-1)
        result=cf(num)
        return render(request,'facterial.html',{'result':result})
    return render(request,'facterial.html')

def cs(string):
    c=0
    for ch in string:
        c=c+1
    return c
def sl(request):
    sl=None
    if request.method=='POST':
        user_input=request.POST.get('user_input','')
        sl=cs(user_input)
    return render(request,'strlength.html',{'sl':sl})

def replace(request):
    replaced_text=""
    if request.method=='POST':
        text=request.POST.get('input_text','')
        old_word=request.POST.get('old_word','')
        new_word=request.POST.get('new_word','')

        replaced_text=text.replace(old_word,new_word)

    return render(request,'replace.html',{'replaced_text':replaced_text})


    

def removedup(request):
    modified_text=''
    if request.method=='POST':
        input_text=request.POST.get('input_text','')
        words=input_text.split()
        unique_words=[]
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
                modified_text=''.join(unique_words)
    return render(request,'removedup.html',{'modified_text':modified_text})


# def concatelist(request):
#     list1=[1,2,3,4,5]
#     list2=['aptech','btm','india']
#     return render(request,'concatelist.html',{'list1':list1,'list2':list2})


def concatelist(request):
    
    if request.method=='POST':
        text=request.POST.get('input_text')
        text1=request.POST.get('input_text1')
        result=text+text1
        return render(request,'concatelist.html',{'result':result})
    return render(request,'concatelist.html')
        
    

# def revesed(request):
#     rev=''
#     if request.method=='POST':
#         text=request.POST.get('input_text')
#         rev=text[::-1]

#     return render(request,'revesed.html',{'rev':rev})


# def revesed(request):
#     rev=''
#     if request.method=='POST':
#         text=request.POST.get('input_text')
#         rev=text[::-1]

#     return render(request,'revesed.html',{'rev':rev})

# with built_in method
def reverse(s):
    return ''.join(reversed(s))
def revesed(request):
    rev=''
    if request.method=='POST':
        text=request.POST.get('input_text')
        rev=reverse(text)

    return render(request,'revesed.html',{'rev':rev})



def setcookie(request):
    response= render(request,'setcookie.html')
    response.set_cookie('name','sai')
    return response


from datetime import datetime ,timedelta

def setcookie1(request):
    response=render(request,'setcookie.html')
    ex=datetime.now()+timedelta(seconds=40)
    response.set_cookie('name','apptechknow',expires=ex)
    return response

def getcookie(request):
    name=request.COOKIES['name']
    return render(request,'getcookie.html',{'name':name})


def secondlargest(request):
    l= [1, 2, 3, 4, 15, 6] 
    f=l[0]
    s=l[0]
    for i in range(len(l)):
        if l[i] > f:
            s = f
            f = l[i]
        elif l[i] > s:
            s =l[i]

    return render(request, 'secondlargest.html', {'second_largest_number': s,'l':l})
    

    
def ses(request):
    visit_count=request.session.get('visit_count',0)
    visit_count+=1
    request.session['visit_count']=visit_count
    return render(request,'sesstion.html',{'visit_count':visit_count})


def ses1(request):
    visited=request.session.get




def exception(request):
    apt={}
    if request.method == 'POST':
        num1=int(request.POST.get('num1'))
        num2=int(request.POST.get('num2'))
        try:
            result=num1//num2
            apt['result']=result
        except ZeroDivisionError:
            apt['error']='Error Division by zero is not allowed'
    return render(request,'exception.html',apt)


def exception_array(request):
    
   
    if request.method == 'POST':
        num1=request.POST.get('num1')
        a=num1.split(',')
        try:
            index=int(request.POST.get('index',1))
            Element=a[index]
        except (ValueError,IndexError):
            Element=None
        return render(request,'exception_array.html',{'Element':Element,'index': index})
        
    return render(request,'exception_array.html')



# 1.write a program to change given string to new string  where first letter chande last letter

def ex1(request):
    if request.method == 'POST':
        s=request.POST.get('num1')
        f=s[0]
        l=s[-1]
        c=l+s[1:-1]+f
        return render (request,'ex1.html',{"c":c})
    return render (request,'ex1.html')

# 2.Write a program to count the number 4 in a given list

def ex2(request):
    l=[1,2,3,4,5,6,7,8,4,4]
    c=0
    s=4
    for i in l:
        if i == s:
            c=c+1
    return render (request,'ex2.html',{'c':c,'l':l})
    
# 3.Write a  program which accepts the radius of a circle from the user and compute the area

def ex3(request):
    r=1
    area=22/7*r*r
    return render(request,'ex3.html',{'area':area})



#4.Write a program to count the number of characters (character frequency) in a string

def ex4(request):
    s='saisiva'
    v={}
    for i in s:
        if i in v:
            v[i]+=1
        else:
            v[i]=1
    
       
    return render(request,'ex4.html',{'v':v,'s':s})
    


# 5.Write a program to count the occurrences of each word in a given sentence

def ex5(request):
    s = "sai siva sankar vara prasad gowd sai siva sankar"
    s1=s.split()

    v={}
    for i in s1:
        c=i.strip('.,!?').lower()
        if c in v:
            v[c]+=1
        else:
            v[c]=1
    return render(request,'ex5.html',{'v':v,'s':s})





# 6. Write a program to check number is Armstrong or not.
def ex6(request):
    n=154

   
    temp=n
    rev=0
    while temp>0:
        d=temp%10
        rev=rev+d*d*d
        temp=temp//10
    return render(request,'ex6.html',{'rev':rev,'n':n})




def slug1(request,sid):
    return render(request,'slug1.html',{'sid':sid})



def slug2(request,slug):
    data={
        'title':'page details',
        'content':f'this is details page for{slug}'
    }
    return render(request,'slug2.html',data)



def slug3(request,slug):
    if slug=='apptech':
        content='sai'
    else:
        content='page is not found'
    return render(request,'slug3.html',{'content':content})


def slug4(request,slug):
    if slug =='java':
        return render(request,'slug4.html')
    else:
        return render (request,'page2.html')



def slug5(request):
    return render(request,'slug5.html')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from django.http import JsonResponse


def json1(request):
    message={'message':'hello from django'}
    return JsonResponse(message)


# pip instal psutil
# import pstutil
# import platform

import psutil
import platform
def psutil(request):
    client_ip=request.META.get('REMOTE_ADDR','')
    os_info={
        'system':platform.system(),
        'release':platform.release(),
        'version':platform.version(),
        'machine':platform.machine(),
        'processor':platform.processor(),
    }
    '''
    django_version={
        'version':django.get_version(),
    }
    '''
    system_info_data={
        'ip_address':client_ip,
        'os_info':os_info,
        #'django_version':django_version,
    }
    return JsonResponse(system_info_data)


# GET AND POST THROUGHT JSON   
from django .http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET,require_POST
import json 

@require_GET
def get_example(request):
    return JsonResponse({'message':'this is GET example'})

@csrf_exempt
@require_POST
def post_example(request):
    try:
        data_received = json.loads(request.body.decode('utf-8'))
        response_data = {
            'message': 'This is a POST request example.',
            'dataReceived': data_received
        }
        return JsonResponse(response_data)
    except json.JSONDecodeError:
        return


#CRUD OPERATION 
# 1.modlo division and find cofficent of reminder
# 2.automoriphic
#3.enumerating consecative words

data=[]
def index(request):
    return render(request,'index.html',{'data':data})

def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        data.append({'name':name,'address':address})
        return redirect('index')
    return render(request,'create.html')


def update(request,index):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        data[index]={'name':name,'address':address}
        return redirect('index')
    return render(request,'update.html',{'record':data[index]})

def delete(request,index):
    del data[index]
    return redirect('index')



###########
#from .forms import FileForm

def read(request):
    file_path='myfile.txt'
    try:
        with open(file_path,'r') as file:
            content=file.read()
            
    
    
    except FileNotFoundError:
        
        content=''
    
    return render (request,'read_file.html',{'content':content})
   


def write(request):
    if request.method=='POST':
        form=FileForm(request.POST)
        if form.is_valid():
            content=form.cleaned_data['content']
            file_path='myfile.txt'
            with open(file_path,'w')as file:
                file.write(content)
            return redirect('read_file')
    else:
        form=FileForm()
    return render(request,'write_file.html',{'form':form})


def append(request):
    if request.method=='POST':
        form=FileForm(request.POST)
        if form.is_valid():
            content=form.cleaned_data['content']
            file_path='myfile.txt'
            with open(file_path,'a')as file:
                file.write(content)
            return redirect('read_file')
    else:
        form=FileForm()
    return render(request,'append_file.html',{'form':form})





def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if not name or not email or not password or not confirm_password:
            error_message='All fields are required'
            return render(request,'registration.html',{'error_message':error_message})

        if password!=confirm_password:
            error_message='Password do not match'
            return  render(request,'registration.html',{'error_message':error_message})

        welcome_message= f"welcome,{name}"

        return redirect('success1.html',welcome_message=welcome_message)

    return render(request,'registration.html')


def success1(request):
    return render(request,'success1.html',{'welcome_message':welcome_message})



#==================================================================

import re

def reg1(request):
    my_str='bangaluru'
    occurrences_of_r=re.findall('r',my_str)
    apt={'occurrences_of_r':occurrences_of_r}
    return render (request,'reg1.html',apt)


def reg2(request):
    my_str='welcome to all students'
    mathes=re.findall('e',my_str)
    apt={'count':len(mathes)}
    return render (request,'reg2.html',apt)

def search(request):
    my_str='welcome to all'
    pattern='all'
    result='pattern found' if re.search(pattern,my_str) else 'pattern not found'
    #return render(request,'search.html',{'result':result})
    return HttpResponse(result)



def reg3(request):
    my_str='welcome to all students'
    split_result=re.split(' ',my_str,3)
    contex={'split_result':split_result}
    return render (request,'reg3.html',contex)

def reg4(request):
    my_str='welcome to all students'
    split_result=re.sub('e','E',my_str,3)
    contex={'split_result':split_result}
    return render (request,'reg4.html',contex)

def check_mobile_number(request):
    if request.method=='POST':
        mobile_number=request.POST.get('mobile_number')
        contex={
            'mobile_number':mobile_number
        }
        if re.match(r'^9\d{9}$',mobile_number):
            contex['is_validate_mobile_number']=True
        else:
            contex['is_validate_mobile_number']=False
        return render(request,'mobile_number.html',contex)
    return render(request,'mobile_number.html',{'mobile_number':''})


from django.views.generic import TemplateView

# opps

class CalculatorView(TemplateView):
    template_name='calculator.html'

    def post(self,request):
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        result=num1+num2
        return self.render_to_response({'result':result})


class SweepView(TemplateView):
    template_name='sweep(opps).html'

    def post(self,request):
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        result=num1
        num1=num2
        num2=result
        
        return self.render_to_response({'num1':num1,'num2':num2})


class Hook2view(TemplateView):
    template_name='Hook2view.html'

    def get_context_data(self):
        context={'click_count':0}
        return context



def bankaccount(request):
    if request.method=='POST':
        a=request.POST.get('account_number')
        b=request.POST.get('balance')
        en=Enquiry(account_number=a,balance=b)
        en.save()
    
    return render (request,'bankaccount.html')




# step1:python manage.py migrate
#  python manage.py createsuperuser
#   username,password,ypython manage.py runserver
#  local host admin
# step2:django-admin startapp formvalidation
# step3:

from formvalidation.models import*

def value1(request):
    if request.method=="POST":       
        a= request.POST.get('name')
        b= request.POST.get('email')
        c= request.POST.get('password')
        d= request.POST.get('birthdate')
        e= request.POST.get('gender')
        en=Enquiry(name=a,email=b,password=c,birthdate=d,gender=e)
        en.save()
    return render(request,"formvalidation.html")


#========================================json

def add_number(request,num1,num2):
    num1=int(num1)
    num2=int(num2)
    result=num1+num2
    return HttpResponse(f'the sum of {num1} and {num2}is{result}')

def sweep_number(request,num1,num2):
    num1=int(num1)
    num2=int(num2)
    num1,num2=num2,num1
    response_data={'num1':num1,'num2':num2}
    return JsonResponse(response_data)

def sum_digit(request,number):
    number=int(number)
    sum_result=0
    while number>0:
        sum_result=sum_result+number%10
        number=number//10
    response_data={'sum':sum_result}
    return JsonResponse(response_data)











                     


































def pra(request):
    if request.method == 'POST':
        s=request.POST.get('num1')
        f=s[0]
        l=s[-1]
        c=l+s[1:-1]+f
        return render (request,'pra.html',{"c":c})
    return render (request,'pra.html')


    

def menubar(request):
    return render(request,'menubar.html')
    
def payment(request):
    return render(request,'payment.html')

def project(request):
    return render(request,'project.html')

   # views.py

from .forms import SignInForm


def project2(request):
    return render(request,'project2.html')

    # if request.method == 'POST':
    #     form = SignInForm(request.POST)
    #     if form.is_valid():
    #         # Add your authentication logic here
    #         # Redirect to the appropriate page after successful login
    #         return redirect('formvalidation')
    # else:
    #     form = SignInForm()

    # return render(request, 'project2.html', {'form': form})

    






























































































































    









# project
def froendpage(request):
    return render(request,'froendpage.html')
def chatbox(request):
    return render(request,'chatbox.html')

def formvalidation(request):
    return render(request,'formvalidation.html')

def loginpage(request):
    return render(request,'loginpage.html')

def login_signup(request):
    if request.method == 'POST':
        # Handle login or signup form submissions here
        # Use request.POST to access form data

        if 'newUser' in request.POST:
            # Handle signup
            name = request.POST['name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            # Create a new user and log them in
            user = User.objects.create_user(username, email, password)
            user.first_name = name
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            return redirect('lcm.html')

        elif 'existingUser' in request.POST:
            # Handle login
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            return redirect('lcm.html')

    return render(request, 'loginpage.html')













































