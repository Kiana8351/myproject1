from django.shortcuts import render

def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')
def contact_page(request):
    return render(request,'contact.html')

def test_view(request):
    context = {'title':'test','body':'this is a test'}
    return render(request,'test.html',context)