from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.db.models import Q
from signin.forms import MyRegistrationForm
import re

# Create your views here.

from .forms import AdPostForm
from .models import PostTable

def adpost(request):
    if request.method == 'POST':
        form = AdPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/post_success/')
        else:
            return HttpResponseRedirect('/post_invalid/')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = AdPostForm()
    
    return render_to_response('adPost.html', args)


def homemm(request):
    return render_to_response('adPost.html',
                              {'username': request.user.username})


def posts_view(request):
    args ={}
    args.update(csrf(request))
    
    args['posts_view'] = PostTable.objects.all().order_by('-Post_Date', '-Product_ID')
    
    return render_to_response('posts_view.html', args)  


def post_view(request, U_ID="Sujay"):
    return render_to_response('post_view.html', 
                              {'posts_view': PostTable.objects.filter(User_ID=U_ID)})


def post_success(request):
    return render_to_response("post_success.html",
                              locals(),
                              context_instance=RequestContext(request),)


def post_invalid(request):
    return render_to_response('post_invalid.html')


def search_posts(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
    args ={}
    args.update(csrf(request))

    args['posts_view'] = PostTable.objects.filter(Title__contains=search_text)    
    return render_to_response("search.html", args)


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['Title', 'User_ID', 'Description',])
        
        found_entries = PostTable.objects.filter(entry_query).order_by('-Post_Date')

    return render_to_response('search.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in indivdual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1] or t[2]).strip()) for t in findterms(query_string)] 


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query