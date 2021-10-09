from django.urls import path , include
from . import views
app_name="app"
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('', views.index, name="index"),
    path('editprofile', views.editProfile, name="edit-profile"),
    path('members/', views.members, name="members"),
    path('register/',views.Register,name="register"),
    path('login/',views.loginView,name="login"),
    path('logout/',views.logoutView,name="logout"),
    path('add/<int:id>',views.addfriend,name="add-friend"),
    path('newRequest/',views.newRequest,name="new-request"),
    path('confirmRequest/<int:id>',views.confirmfriend,name="confirm-request"),
    path('ok/<int:id>',views.ok,name="ok-request"),
    path('messages/',views.messages,name="msg"),
    path('sendMessage/<int:id>',views.sendMessage,name="msg_send"),
    path('forums/',views.forums,name="forums"),
    path('forums/<int:id>',views.groupe,name="join-group"),
 
    path('about/',views.about ,name="about"),
    

]