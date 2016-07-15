from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from places.serializers import CategorySerializer

from places.forms import LoginForm
from places.models import Category

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@login_required
def home(request):
    data = {}
    return render_to_response('index.html', data, context_instance=RequestContext(request))


################################################
#                                              #
#               REST APIs                      #
#                                              #
################################################

@csrf_exempt
def category_list(request):
    """
    List all code categories, or create a new category.
    """
    if request.method == 'GET':
        categories = Category.objects.all()	
        serializer = CategorySerializer(categories, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    """
    functions retrieves, updates or deletes a category.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)


################################################
#                                              #
#               LOGIN/LOGOUT                   #
#                                              #
################################################
def login_page(request):
    message = error = None
    username = password = ''
    form = LoginForm()

    # default next page is index page
    next_page = "/"

    # getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        # a form bound to the post data
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"

                # redirect after post
                return HttpResponseRedirect(next_page)
            else:
                message = "Your account is not active, please contact the site admin."
                error = 1
        else:
            message = "Your username and/or password were incorrect."
            error = 1

    c = {'username': username, 'form': form, 'next': next_page}
    if message:
        c.update({"message": message})
    if error:
        c.update({"error": error})
    c.update(csrf(request))

    return render_to_response('login.html', c)


def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request': request})
