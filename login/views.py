from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from .forms import SignUpForm, LoginForm
import json

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

# Create your views here.

@require_POST
def login_api(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                #return redirect('home')
                return JsonResponse({'detail': 'Logged in'})
            
            else:
                form = LoginForm()
            return render(request, 'login.html', {'form' : form})
        

#       return JsonResponse(data)


def logout_api(request):
    logout(request)
    return JsonResponse({'detail': 'Logged Out Successfully.'})


@ensure_csrf_cookie
def session_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})
    
    return JsonResponse({'isAuthenticated': True})



#    if request.method == 'GET':
#        data = {
#            'username': 'myusername',
#            'password': 'mypassword123'
#       }
#        return JsonResponse(data)
    
#    elif request.method == 'POST':
#        try:
#            data = json.loads(request.body)
            
#        except json.JSONDecodeError:
#            return HttpResponseBadRequest('The format was not correct.')
        
#        loginform = LoginForm(data)
#        if loginform.is_valid():
#            username = loginform.cleaned_data['username']
#            password = loginform.cleaned_data['password']

#            return JsonResponse({'message': 'The data was received.'})

#        else:
#            errors = dict(loginform.errors.items())
#            return JsonResponse({'errors': errors}, status=400)

#@api_view(['POST'])

#def loginuser(request):
#    user = get_object_or_404(User, username=request.data['username'])
#    if not user.check_password(request.data['password']):
#        return Response({"detail:" "Not found."}, status=status.HTTP_404_NOT_FOUND)
#    token, newcreate = Token.objects.get_or_create(user=user)
#    serializer = UserSerializer(instance=user)
#    return Response({"token": token.key, "user": serializer.data})
