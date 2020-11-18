from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group


# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'home/index.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'parents/adminclick.html')


def parentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'parents/parentclick.html')

def parent_signup_view(request):
    userForm=forms.ParentUserForm()
    parentForm=forms.ParentForm()
    mydict={'userForm':userForm,'parentForm':parentForm}
    if request.method=='POST':
        userForm=forms.ParentUserForm(request.POST)
        parentForm=forms.ParentForm(request.POST,request.FILES)
        if userForm.is_valid() and parentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            parent=parentForm.save(commit=False)
            parent.user=user
            parent.assignedDoctorId=request.POST.get('assignedDoctorId')
            parent=parent.save()
            my_parent_group = Group.objects.get_or_create(name='PARENT')
            my_parent_group[0].user_set.add(user)
        return HttpResponseRedirect('parentlogin')
    return render(request,'parents/parentsignup.html',context=mydict)


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_parent(user):
    return user.groups.filter(name='PARENT').exists()



def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'doctor/doctor_wait_for_approval.html')
    elif is_parent(request.user):
        #accountapproval=models.Parent.objects.all().filter(user_id=request.user.id,status=True)
        #if accountapproval:
            return redirect('parent-dashboard')
        #else:
            #return render(request,'parents/parent_wait_for_approval.html')

@login_required(login_url='parentlogin')
@user_passes_test(is_parent)
def parent_dashboard_view(request):
    parent=models.Parent.objects.get(user_id=request.user.id)
    #doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
    userForm=forms. AddChildForm()
    parentForm=forms. AddChildForm()
    mydict={'AddChildForm':userForm,'parentForm':parentForm}
    #mydict={
    #'parent':parent,
    #'doctorName':doctor.get_name,
    #'doctorMobile':doctor.mobile,
    #'doctorAddress':doctor.address,
    #'symptoms':parent.symptoms,
    #'doctorDepartment':doctor.department,
    #'admitDate':parent.admitDate,
    #}
    return render(request,'parents/parent_dashboard.html',context=mydict)


@login_required(login_url='parentlogin')
@user_passes_test(is_parent)
def addchild(request):
    if is_parent(request.user):
        #parent=models.Parent.objects.get(user_id=request.user.id)
        userForm=forms. AddChildForm()
        #parentForm=forms.ParentForm()
        #parentForm=forms. AddChildForm()
        mydict={'AddChildForm':userForm}
        #parent=Parent.objects.get(pk=parent.id)

        if request.method=='POST':
            childForm=forms.AddChildForm(request.POST)
            #parentForm=forms.AddChildForm(request.POST,request.FILES)
            if childForm.is_valid():
                #text=userForm.cleaned_data()
                newest=childForm.save(commit=False)
                newest.parent=request.user
                newnum= 2
                #childid="C"."I".rand(10, 20).date('s').newnum.chr(rand(65, 90))
                newest.save()

    return render(request, 'parents/parent_dashboard_cards.html',context=mydict)

@login_required(login_url='parentlogin')
@user_passes_test(is_parent)
def view_child(request):
    #user_id=request.user.id
    children=models.Child.objects.all().filter(parent_id=request.user.id)
    context={
    "children":children
    }
    return render(request, 'parents/parent_view_child.html', context)
