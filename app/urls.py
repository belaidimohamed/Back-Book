from django.urls import path , include
from . import views
app_name="app"
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('', views.index, name="index"),
    path('editprofile', views.editProfile, name="edit-profile"),
    path('messages/', views.messages, name="msg"),
    path('members/', views.members, name="members"),
    path('register/',views.Register,name="register"),
    path('login/',views.loginView,name="login"),
    path('logout/',views.logoutView,name="logout"),
    path('add/<int:id>',views.addfriend,name="add-friend"),
    path('newRequest/',views.newRequest,name="new-request"),
]