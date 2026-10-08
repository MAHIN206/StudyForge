from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'subjects/',
        views.subjects,
        name='subjects'
    ),

    path(
        'subjects/create/',
        views.create_subject,
        name='create_subject'
    ),

    path(
        'notes/',
        views.notes,
        name='notes'
    ),

    path(
        'notes/create/',
        views.create_note,
        name='create_note'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

]