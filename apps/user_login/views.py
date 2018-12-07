from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'user_login/index.html')


def create(request):
    errors = []
    print(request.POST)
    if request.POST == 'POST':
        if len(request.POST['first_name']) <1:
            errors.append('First name must be more than 2 characters')
        else:
            pass


    return redirect('/')
