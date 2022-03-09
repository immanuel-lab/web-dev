
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
path('',views.home,name='home'),

path('form/',views.forms,name='form'),
path('formsub',views.form_submission,name='formsub'),

path('register/',views.register,name='register'),
path('navbar/',views.navbar,name='navbar'),

path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
path('profile/',views.profile,name='profile'),

# CHANGE PASSWORD
path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html'),name='change_password'),
path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='password_change_done'),

#password reset
#provides form
path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),



#redirect after sending email
path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),


#send email

path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
#success message
path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

path('socialmedialog/',views.socialmedlog,name='socialmedialog'),

path('visit/',views.visit,name='visit'),

path('editor/',views.editor,name='editor'),
path('editorsave',views.cked_save,name='editorsave'),

path('salvation/',views.salv,name='salvation')
]


