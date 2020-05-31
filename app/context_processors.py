from django.shortcuts import get_object_or_404 
from .models import Friends , Messages , UserProfile


def notification(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    l=[]
    try:
        friends = Friends.objects.all().filter(user=profile,confirmed=False)
    except :
        friends = None
    for friend in friends :
        print(friend)

        profile = get_object_or_404(UserProfile,user=friend.friend)
        l.append((friend,profile))
    return {'friends': l}

