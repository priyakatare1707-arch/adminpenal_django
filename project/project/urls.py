
"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing,name='landing'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    # path('login_data/',views.login_data,name='login_data'),
    path('admindashboard/',admindashboard,name='admindashboard'),
    path('admindashboard/add_dep/',add_dep,name='add_dep'),
    path('admindashboard/show_dep/',show_dep,name='show_dep'),
    path('admindashboard/save_dep/',save_dep,name='save_dep'),
    path('admindashboard/add_emp/',add_emp,name='add_emp'),
    path('admindashboard/save_emp/',save_emp,name='save_emp'),
    path('admindashboard/show_emp/',show_emp,name='show_emp'),
    path('admindashboard/emp_all_query/',emp_all_query,name='emp_all_query'),
    path('admindashboard/emp_all_query/reply/<int:pk>/',reply,name='reply'),
    path('admindashboard/emp_all_query/a_reply/<int:pk>/',a_reply,name='a_reply'),
    path('empdashboard/',empdashboard,name='empdashboard'),
    path('empdashboard/profile/',profile,name='profile'),
    # path('empdashboard/settings/',settings,name='settings'),
    path('empdashboard/edit_profile/',edit_profile,name='edit_profile'),
    path('empdashboard/empquery/',empquery,name='empquery'),
    path('empdashboard/querydata/',querydata,name='querydata'),
    path('empdashboard/allquery/',allquery,name='allquery'),
    path('empdashboard/pendingquery/',pendingquery,name='pendingquery'),
    path('empdashboard/donequery/',donequery,name='donequery'),
    path('empdashboard/all_query/emp_q_edit/<int:pk>/',emp_q_edit,name='emp_q_edit'),
    path('empdashboard/all_query/emp_q_delete/<int:pk>/',emp_q_delete,name='emp_q_delete'),
    path('empdashboard/all_query/updated_querydata/<int:pk>/',updated_querydata,name='updated_querydata'),
    path('empdashboard/all_query/search/',search,name='search'),
    path('empdashboard/all_query/reset/',allquery,name='reset'),
    path('admindashboard/add_item/',add_item,name='add_item'),
    path('admindashboard/show_items/',show_items,name='show_items'),
    path('admindashboard/show_items/paynow/<int:pk>/',paynow,name='paynow'),
   
    path('pay_amount/',pay_amount,name='pay_amount'),
     path('success/',success,name='success')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)