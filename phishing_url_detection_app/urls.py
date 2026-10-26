from django.urls import path  
from . import views
urlpatterns=[ 
    path('',views.homepage),
    path('url_pred',views.url_predict)    
]
