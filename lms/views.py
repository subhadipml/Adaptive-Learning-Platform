from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'lms/index.html')
def login(request):
    return render(request, 'lms/login.html')
def signup(request):
    return render(request, 'lms/signup.html')

def user_created(request):
    if request.method=='GET':
        saverecord = User()
        saverecord.username = request.GET.get('username')
        saverecord.role = request.GET.get('role')
        saverecord.emailid = request.GET.get('emailid')
        saverecord.password = request.GET.get('password')
        saverecord.save()
        # messages.success(request, "Record saved successfully....")
        return render(request, 'lms/confirmed.html')
    # else:
    #     return render(request, 'lms/signup.html')
    return render(request, 'lms/signup.html')
    # return render(request, 'lms/signup.html', {'username': username, 'role': role, 'emailid': emailid, 'password': password})
    # return render(request, 'lms/signup.html')

def dashboard(request):
    if request.method=='GET':
        userdetails = User.objects.all()
        loginemailid = request.GET.get('emailid')
        loginpassword = request.GET.get('password')
        flag = False
        currentUserName, currentUserRole, currentUserEmailId = None, None, None
        for i in userdetails:
            if i.emailid==loginemailid and i.password==loginpassword:
                currentUserName = i.username
                currentUserRole = i.role
                currentUserEmailId = i.emailid
                flag = True
                break
        # if(loginemailid in user)
        if flag==True:
            return render(request, 'lms/dashboard.html', {'currentUserName': currentUserName, 'currentUserRole': currentUserRole, 'currentUserEmailId': currentUserEmailId})
        else:
            return render(request, 'lms/notconfirmed.html')
    # else:
    #     return render(request, 'lms/signup.html')
    return render(request, 'lms/login.html')