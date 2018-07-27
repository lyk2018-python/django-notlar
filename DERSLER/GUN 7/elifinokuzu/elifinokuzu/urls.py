from django.contrib import admin
from django.urls import path, include
from dictionary import views as dictionary_views
from accounts import views as account_views
from comments import views as comment_views

urlpatterns = [
    path('', dictionary_views.home, name='home'),
    path('about/', dictionary_views.about, name='about'),
    path('support/', dictionary_views.support, name='support'),
    path('admin/', admin.site.urls),
    path('nodes/<int:id>/', dictionary_views.node_detail, name='node_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', account_views.signup, name='signup'),
    path('accounts/profile/', account_views.dashboard, name='dashboard'),
    path('submit/', dictionary_views.submit, name='submit' ),
    path('nodes/<int:id>/comment/', comment_views.add_comment_to_node, name='add_comment_to_node'),
]
