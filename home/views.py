from django.shortcuts import render


# Home View
def get_index(request):
    return render(request,'index.html')


# About View
def get_about(request):
    return render(request,'about.html')


# Contact View
def get_contact(request):
    return render(request,'contact.html')
