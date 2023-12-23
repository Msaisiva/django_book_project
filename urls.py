"""
URL configuration for apt1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apt1 import view
from .view import get_example, post_example
from.view import CalculatorView
from.view import SweepView
from.view import Hook2view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sai/',view.homepage),
    path('sai/',view.localvariable),
    path('sai1/',view.globalvariable),
    path('get/',view.getandpost),
    path('add/',view.add),
    path('login/',view.login),
    path('apt/',view.grade_form),
    path('wel',view.sai),
    path('local',view.localvariable),
    path('gp',view.gp),
    path('add1',view.add),
    path('login1',view.login1),
    path('page2',view.page2,name='page2'),
    path('page4',view.page4,name='page4'),
    path('database',view.value),
    path('for',view.student_result),
    path('even',view.even),
    path('eliif',view.student_result),
    path('eliif1',view.grade),
    path('eliif2',view.big),
    path('eliif3',view.posstive),
    path('eliif4',view.simple),
    path('table',view.table),
    path('atm',view.atm),
    path('sweep',view.sweep),
    path('pra',view.pra),
    path('lcm',view.lcm),
    path('perfect',view.perfect),
    path('gcd',view.gcd),
    path('vowelcount',view.vowelcount),
    path('cf',view.fact),
    path('cs',view.sl),
    path('replace',view.replace),
    path('removedup',view.removedup),
    path('froendpage',view.froendpage),
    path('loginpage',view.loginpage),
    path('loginpage1',view.login_signup),
    path('payment',view.payment),
    path('chatbox',view.chatbox),
    path('formvalidation',view.formvalidation,name='formvalidation'),
    path('concatelist',view.concatelist),
    path('revesed',view.revesed),
    path('setcookie',view.setcookie),
    path('setcookie1',view.setcookie1),
    path('getcookie',view.getcookie),
    path('secondlargest',view.secondlargest),
    path('ses',view.ses),
    path('exception',view.exception),
    path('exception_array',view.exception_array),
    path('ex1',view.ex1),
    path('ex2',view.ex2),
    path('ex3',view.ex3),
    path('ex4',view.ex4),
    path('ex5',view.ex5),
    path('ex6',view.ex6),
    path('slug1/<int:sid>/',view.slug1,name='slug1'),
    path('slug2/<slug:slug>/',view.slug2,name='slug2'),
    path('slug3/<slug:slug>/',view.slug3,name='slug3'),
    path('slug4/<slug:slug>/',view.slug4,name='slug4'),
    path('slug5',view.slug5),
    path('json1',view.json1),
    path('psutil',view.psutil),
    path('get_example',view.get_example),
    path('post_example', post_example, name='post_example'),
    path('index1', view.index, name='index'),
    path('create/', view.create, name='create'),
    path('update/<int:index>/',view. update, name='update'),
    path('delete/<int:index>/', view.delete, name='delete'),
    path('project',view.project),
    path('project2',view.project2),
    path('read',view.read,name='read_file'),
    path('write',view.write,name='write_file'),
    path('append',view.append,name='append_file'),
    path('registration',view.registration,name=' registration'),
    path('success1/<str:welcome_message>/',view.success1,name='success1'),
    path('reg1',view.reg1),
    path('reg2',view.reg2),
    path('search',view.search,name='search'),
    path('reg3',view.reg3),
    path('reg4',view.reg4),
    path('check-mobile-number/', view.check_mobile_number, name='check-mobile-number'),
    path('calculator',CalculatorView.as_view(),name='CalculatorView'),
    path('sweepopps',SweepView.as_view(),name='SweepView'),
    path('Hook2view',Hook2view.as_view(),name='Hook2view'),
    path('menubar',view.menubar),
    path('bankaccount',view.bankaccount),
    path('database1',view.value1),
    path('add/<int:num1>/<int:num2>/',view.add_number),
    path('sweep/<int:num1>/<int:num2>/',view.sweep_number),
    path('sum_digit/<int:number>/',view.sum_digit),
    

    






]



