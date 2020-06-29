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
from django.contrib.auth.decorators import login_required


register = template.Library()

#--------------------------------------------------- Account -------------------------------------------------

def index(request):

    return render(request, 'app/index.html')


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



@login_required
def logoutView(request):
    logout(request)
    return redirect('app:index')

def profile(request):
    try:
        profile = get_object_or_404(UserProfile,user=request.user)
    except :
        redirect('app/edit_profile.html')
    profile1 = profile
    l=[]
    try:
        friends = Friends.objects.all().filter(user=profile,confirmed=True)
    except :
        friends = None
    for friend in friends :
        profile = get_object_or_404(UserProfile,user=friend.friend)
        l.append((friend,profile))

    return render(request, 'app/profile.html',{'all_friends':l,'profile':profile1})

#---------------------------------------- NavBar methodes -----------------------------------------------
def sendMessage(request,id):
    print('i am here')
    profile = get_object_or_404(UserProfile,user=request.user)
    l=[]
    try:
        friends = Friends.objects.all().filter(user=profile,confirmed=True)
    except :
        friends = None
    for friend in friends :
        profile = get_object_or_404(UserProfile,user=friend.friend)
        l.append((friend,profile))

    friend = Friends.objects.get(id=id,confirmed=True)
    profile = get_object_or_404(UserProfile,user=friend.friend)
    print(friend.messages)
    #................................
    if request.POST :
        msg = request.POST['message']
        print(msg)
    return render(request, 'app/messageSend.html',{'Mfriends':l,'friend':(friend,profile),'id':id}) 
    
def messages(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    l=[]
    try:
        friends = Friends.objects.all().filter(user=profile,confirmed=True)
    except :
        friends = None
    for friend in friends :
        profile = get_object_or_404(UserProfile,user=friend.friend)
        l.append((friend,profile))

    return render(request, 'app/messages.html',{'Mfriends':l})

def newRequest(request):
    
    return render(request, 'app/new_requests.html')

def members(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    print(profile)
    list_of_friends=[]
    try:
        friends = Friends.objects.all().filter(user=profile)
        for friend in friends:
            list_of_friends.append(friend.friend)
    except :
        friends = None
    users = User.objects.all()
    l=[]
    for user in users :
        if user!=request.user:
            if user in list_of_friends :
                print('fuck') 
                continue
            else :
                try:
                    profile = UserProfile.objects.get(user=user)
                    l.append((user,profile))
                except:
                    continue
            

    return render(request, 'app/members.html',{'users_p':l})

def addfriend(request,id):
  
    friend = get_object_or_404(User,id=id)
    profile = get_object_or_404(UserProfile,user=friend) #adding friend (not confirmed) to the target
    obj = Friends()
    obj.user = profile
    obj.friend = request.user
    obj.confirmed = False
    obj.save()

    profile = get_object_or_404(UserProfile,user=request.user) #adding friend (not confirmed) to the requester
    obj1= Friends() 
    obj1.user = profile
    obj1.friend = friend
    obj1.confirmed = False
    obj1.Isent = True 
    obj1.save()
    return render(request, 'app/members.html')

def confirmfriend(request,id):
  
    friend = get_object_or_404(User,id=id)
    profile = get_object_or_404(UserProfile,user=request.user)
    obj = Friends.objects.get(user=profile,friend=friend)
    obj.confirmed = True
    obj.save()

    profile = get_object_or_404(UserProfile,user=friend)
    obj1 = Friends.objects.get(user=profile,friend=request.user)
    obj1.confirmed = True
    obj1.Isent = False
    obj1.accepted = True
    obj1.save()

    return render(request, 'app/members.html')
def ok(request,id):

    friend = get_object_or_404(User,id=id)
    profile = get_object_or_404(UserProfile,user=request.user)
    obj = Friends.objects.get(user=profile,friend=friend)
    obj.accepted = False
    obj.save()
    return render(request, 'app/members.html')