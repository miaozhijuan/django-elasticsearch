"""djangodemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from elasticsearchservice import views
from kgextacttrip import kgviews
from echartsGraph import echartsViews
from userManager import userManagerViews

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('statisticForEcharts/', views.statisticForEcharts),
    path('statisticForIfZLcomplete/', echartsViews.statisticForIfZLcomplete),
    path('statisticForUnitUncomplete/', echartsViews.statisticForUnitUncomplete),
    path('hiddenHistoricalTrend/', echartsViews.hiddenHistoricalTrend),
    path('hiddenReason/', echartsViews.hiddenReason),
    path('hiddenFrom/', echartsViews.hiddenFrom),
    path('hiddenOfficeFrom/', echartsViews.hiddenOfficeFrom),
    path('upload_file/', views.upload_file),
    path('sent_json_to_elasticsearch/', views.sent_json_to_elasticsearch),
    path('processHandleInput/', views.processHandleInput),
    path('kgprocess/', kgviews.kgprocess),
    path('user_add/', userManagerViews.requestUserAdd),
    path('user_delete/', userManagerViews.requestUserDelete),
    path('user_update/', userManagerViews.requestUserUpdate),
    path('user_all/', userManagerViews.requestUserAll),
    path('user_check/', userManagerViews.requestUserCheck),
]
