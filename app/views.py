from django.shortcuts import render , redirect , get_object_or_404 , render_to_response
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView , UpdateView , DeleteView , View , DetailView , ListView
from django.urls import reverse_lazy
from .models import Friends , Messages , UserProfile
from .forms import UserProfileForm , UserForm
from django.contrib.auth.models import User
# Create your views here.
from django import template

register = template.Library()

def messages(request):
    messages = Messages.objects.all()

    return render(request, 'app/messages.html')
def newRequest(request):
    
    return render(request, 'app/new_requests.html')

def members(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    print(profile)
    try:
        friends = Friends.objects.all().filter(user=profile)
    except :
        friends = None
    users = User.objects.all()
    l=[]
    for user in users :
        profile = get_object_or_404(UserProfile,user=user)
        l.append((user,profile))

    return render(request, 'app/members.html',{'users_p':l,'friends':friends})

def addfriend(request,id):
    if not request.user.is_authenticated:
        return redirect('app:index')
    friend = get_object_or_404(User,id=id)
    print('è------------- ',friend)
    profile = get_object_or_404(UserProfile,user=friend)
    obj = Friends()
    obj.user = profile
    obj.friend = request.user
    obj.confirmed = False
    obj.save()
    return render(request, 'app/members.html')

#--------------------------------------------------- Account -------------------------------------------------

def index(request):

    return render(request, 'app/index.html')
def profile(request):
    try:
        profile = get_object_or_404(UserProfile,user=request.user)
    except :
        redirect('app/edit_profile.html')
    friends="fuck"
    return render(request, 'app/profile.html',{'all_friends':friends,'profile':profile})


def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('app:index')
            else:
                return render(request, 'app/account/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'app/account/login.html', {'error_message': 'Invalid login'})
    return render(request, 'app/account/login.html')

def Register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('app:edit-profile')
               
    context = {
        "form": form,
    }
    return render(request, 'app/account/register.html', context)

def logoutView(request):
    logout(request)
    return redirect('app:index')
def editProfile(request):
    if not request.user.is_authenticated:
        return redirect('app:index')

    form = UserProfileForm()
    if request.POST:
        form = UserProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form = UserProfileForm()
            return redirect('app:profile')

    return render(request, 'app/edit_profile.html', {'form':form})