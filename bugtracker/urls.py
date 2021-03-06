"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import login_view, logout_view, add_user
from app2.views import homepage, user_detail, ticket_detail, add_ticket, edit_ticket, assign_ticket, complete_ticket, invalid_ticket
from django.views.static import serve
from django.conf.urls import url
# import settings

urlpatterns = [
    path('user/<int:id>/', user_detail, name='userdetail'),
    path('ticket/<int:id>/', ticket_detail, name='ticketdetail'),
    path('adduser/', add_user, name='adduser'),
    path('addticket/', add_ticket, name='addticket'),
    path('ticket/<int:id>/edit/', edit_ticket, name='editticket'),
    path('ticket/<int:id>/assign/', assign_ticket, name='assignticket'),
    path('ticket/<int:id>/complete/', complete_ticket, name='completeticket'),
    path('ticket/<int:id>/invalid/', invalid_ticket, name='invalidticket'),
    path('', homepage, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STAIC_ROOT}),
]
# urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
