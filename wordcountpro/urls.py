
from . import views 
 
urlpatterns = [
    path('' , views.homepage  , name='home'),
    path('count/', views.count , name='count'), 
    path('aboutpage' , views.about , name='about'),
]