# Users.urls
from django.urls import path

from users import views

urlpatterns = [



    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='singup/',
        view=views.SingupView.as_view(),
        name='singup'
    ),

    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    ),

    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(
            template_name='users/detail.html'
        ),
        name='detail'
    ),

]
