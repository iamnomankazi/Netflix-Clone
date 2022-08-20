from Netflixapp.forms import MembershipEmailForm, SignupForm
from Netflixapp.models import MembershipEmail, Signup, netflix_titles
from django.shortcuts import redirect, render, HttpResponse


# Create your views here.

def Home(request):
    show = netflix_titles.objects.all()
    return render(request, 'index.html', {'show': show})

# info, moviebrowse, updateform, usertable, watchpage
def View(request, pk, cat):
    getmovie = netflix_titles.objects.get(id=pk)
    suggestions = netflix_titles.objects.all().filter(Category=cat)
    return render(request, 'moviepage.html', {'getmovie': getmovie, 'suggestions': suggestions})


def signup(request):
    obj = SignupForm(request.POST)
    
    if obj.is_valid():
        obj.save()
        return redirect('/home/')
    
    return render(request, 'signup.html')


def login(request):
    
    if request.method == 'POST':
        m = Signup.objects.get(CustomerUsername=request.POST['CustomerUsername'])
        print(m)
        
        if m.CustomerPassword == request.POST['CustomerPassword']:
            print('Successfull')
            return redirect('Home')
        else:
            return redirect('login')
        
    return render(request, 'login.html')


def landingpage(request):
    emailform = MembershipEmailForm(request.POST)
    if emailform.is_valid():
        emailform.save()
    return render(request, 'landingpage.html')


def watchpage(request):
    
    return render(request, 'watchpage.html')


def UserDataTable(request):
    users = Signup.objects.all()
    return render(request, 'usertable.html', {'users': users})


def DeleteUser(request, pk):
    selectuser = Signup.objects.get(pk=pk)
    selectuser.delete()
    return redirect('UserDataTable')
    return render(request, 'usertable.html', {'selectuser': selectuser})


def UserUpdate(request, pk):
    selectuser = Signup.objects.get(pk=pk)
    form = SignupForm(request.POST or None, instance=selectuser)
    
    if form.is_valid():
        form.save()
    return redirect('UserDataTable')
    return render(request, 'form.html', {'form': form})


def Infopage(request):
    return render(request, 'info.html')
