from django.shortcuts import render
from online_sites.models import Site,LoginUser

# Create your views here.
def base(request):
    return render(request,'base.html')

def index(request):
    return render(request,'index.html')

def site(request):
    st=Site.objects.all()
    
    print(st)
    context={'st':st}
    return render(request,'site.html',context)

def userlist(request,id):
    st=LoginUser.objects.filter(site_id=id)
    context={'st':st}
    
    return render(request,'user.html',context)