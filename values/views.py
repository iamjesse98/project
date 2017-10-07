from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse,HttpResponseRedirect
from .models import api
from django.core import serializers
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.views import View
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.http.response import StreamingHttpResponse
from .models import api
import datetime

import time

data = []
arr= []
# Create your views here.
@csrf_exempt
def values(request):
    if request.method == 'POST':
        foo_name = api.objects.create(temperature=json.loads((request.body).decode('utf-8')).get('temperature'),
                                      humidity=json.loads((request.body).decode('utf-8')).get('humidity'),
                                      moisture=json.loads((request.body).decode('utf-8')).get('moisture'),
                                      distance=json.loads((request.body).decode('utf-8')).get('distance'), time=datetime.datetime.now().time())
       # data.append(list(map(lambda x: x['fields'], json.loads(serializers.serialize('json', api.objects.all())))))
       # print(api.objects.all())
        #return JsonResponse(json.loads(json.dumps(data).decode('utf-8'))[0], safe=False)
        return JsonResponse(data, safe=False)
    if request.method == 'GET':
        #data = json.loads(json.dumps((request.POST['temperature'])))
        return JsonResponse(list(map(lambda x: x['fields'], json.loads(serializers.serialize('json', api.objects.all())))), safe=False)

@login_required
def gui(request):
    if request.method == 'GET':
        return render(request,'main.html')


def line(request):
    if request.method == 'GET':
        return render(request, 'hist_chart.html')

# def rt(request):
#     if request.method == 'GET':
#         return render(request, 'realtime.html')


def stream_response_generator():
    yield "<html><body>\n"
    for x in range(1, 100):
        yield "<div>%s</div>\n" % x
        yield " " * 10240
        time.sleep(1)
    yield "</body></html>\n"

def rt(request):
    resp = StreamingHttpResponse(stream_response_generator())
    return resp

def login_user(request):
    flag = 0
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and flag == 0:
                login(request, user)
                flag = 1
                #return render(request, 'index.html')
                return HttpResponseRedirect('/values/gui/')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #return render(request,'index.html')
                return HttpResponseRedirect('/values/gui/')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def index(request):
    return render(request, 'index.html')
