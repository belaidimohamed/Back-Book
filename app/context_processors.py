from django.shortcuts import get_object_or_404 ,redirect
from .models import Friends , Messages , UserProfile


def notification(request):
    if not request.user.is_authenticated:
        return {}
    profile = get_object_or_404(UserProfile,user=request.user)
    l=[]
    try:
        friends = Friends.objects.all().filter(user=profile,confirmed=False)
    except :
        friends = None
    for friend in friends :
        profile = get_object_or_404(UserProfile,user=friend.friend)
        l.append((friend,profile))
    return {'friends': l}

