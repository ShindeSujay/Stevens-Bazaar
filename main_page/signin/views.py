from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.core.context_processors import csrf
from forms import MyRegistrationForm


# Create your views here.

def home(request):
    
    return render_to_response("index.html",
                              locals(),
                              context_instance=RequestContext(request),)


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    global signer
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    
    if user is not None:
        auth.login(request, user)
        signer = request.user.username
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Acknowledged.')
            return HttpResponseRedirect('/register_success/')
        else:
            return HttpResponseRedirect('/invalid_email')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = MyRegistrationForm()
    
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response("register_success.html",
                              locals(),
                              context_instance=RequestContext(request),)


def invalid_email(request):
    return render_to_response('invalid_email.html')


def aboutus(request):
    return render_to_response("about-us.html")
    #,
     #                         locals(),
      #                        context_instance=RequestContext(request),)


def firsttime(request):
    return render_to_response('FirstTimeUser.html')


def FAQs(request):
    return render_to_response('FAQs.html')


def team(request):
    return render_to_response('the-team.html')


def terms(request):
    return render_to_response('Terms.html')



