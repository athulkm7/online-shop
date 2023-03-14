from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from backend.models import customer, category, proddetails
from django.http import HttpResponse


def indexhtmlpage(request):
    return render(request,"index.html")
def adminpage(req):
    return render (req,"add admin.html")
def savedata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        Img = request.FILES['image']
        obj = customer(Name=na,Contactnumber=Con,password=pas,Email=Em,username=Us,Image=Img)
        obj.save()
        return redirect(adminpage)
def displayadmin(req2):
    data = customer.objects.all()
    return render(req2, "display.html", {'data':data})
def editstudpage(req,dataid):
    data = customer.objects.get(id=dataid)
    print(data)
    return render(req,"edit.html", {'data':data})
def DeleteData(req, dataid):
    data = customer.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)
def updatedata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = customer.objects.get(id=dataid).Image
        customer.objects.filter(id=dataid).update(Name=na,Contactnumber=Con,password=pas,Email=Em,username=Us,Image=file)
        return redirect(displayadmin)
def addcategory(req):
    return render(req, "add category.html")
def addcat(request):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('discription')
        Img = request.FILES['image']
        obj = category(Name=na,Discription=des, Image=Img)
        obj.save()
        return redirect(addcategory)

def displaycat(req2):
            data = category.objects.all()
            return render(req2, "display category.html", {'data': data})

def editcat(req, dataid):
            data = category.objects.get(id=dataid)
            print(data)
            return render(req, "edit category.html", {'data': data})

def Deletecat(req,dataid):
            data = category.objects.filter(id=dataid)
            data.delete()
            return redirect(displaycat)
def updatecategory(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('discription')
        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = category.objects.get(id=dataid).Image
        category.objects.filter(id=dataid).update(Name=na, Discription=des, Image=file)
        return redirect(displaycat)
def addpropage(req):
    data = category.objects.all()
    return render(req,"add product.html",{'data':data})
def savepro(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        ca = request.POST.get('category')
        Img = request.FILES['image']
        obj = proddetails(Name=na,Desc=de,price=pr,Quantity=qu,Category=ca,Image=Img)
        obj.save()
        return redirect(addpropage)

def dispropage(request):
    data = proddetails.objects.all()
    return render(request,"display product.html",{'data':data})

def editpropage(request,dataid):
    data = proddetails.objects.get(id=dataid)
    da = category.objects.all()
    print(data)
    return render(request,"edit product.html",{'data':data, 'da':da})

def updateprodata(request,dataid):
    if request.method=="POST":
        de = request.POST.get('desc')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        ca = request.POST.get('category')

        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = proddetails.objects.get(id=dataid).Image
        proddetails.objects.filter(id=dataid).update(Desc=de,price=pr,Quantity=qu,Category=ca,Image=file)
        # data = category.objects.all()
        return redirect(dispropage)

def deleteprodata(req,dataid):
    data = proddetails.objects.filter(id=dataid)
    data.delete()
    return redirect(dispropage)

def loginpage(request):
    return render(request,"login.html")

def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password'] = password_r
                return redirect(indexhtmlpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)






