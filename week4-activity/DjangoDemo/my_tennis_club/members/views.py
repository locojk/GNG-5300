from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def login_view(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def register_view(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())