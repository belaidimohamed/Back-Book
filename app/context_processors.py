from django.shortcuts import get_object_or_404 ,redirect
from .models import Friends , Messages , UserProfile


def notification(request):
    if not request.user.is_authenticated:
        return {}
    try :
        profile = get_object_or_404(UserProfile,user=request.user)
    except :
        profile=None
    l=[]
    try:
        friends = Friends.objects.all().filter(user=profile,confirmed=False,Isent=False)
        if not friends :
            friends = Friends.objects.all().filter(user=profile,confirmed=True,Isent=False,accepted=True)
    except :
        friends = None
    for friend in friends :
        profile = get_object_or_404(UserProfile,user=friend.friend)
        l.append((friend,profile))
    return {'friends': l}
