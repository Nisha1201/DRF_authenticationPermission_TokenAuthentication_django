from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# # generate token during request:
# from rest_framework.authtoken.views import obtain_auth_token

# # Using customauthentication:
# from api.auth import CustomAuthToken
# creating router object
router=DefaultRouter()

# ModelViewSet
router.register('studentapi',views.StudentModelViewSet,basename='student')
# router.register('studentapi1',views.StudentModelViewSet2,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),

    # # generate token during request:
    # path('gettoken/',obtain_auth_token)

    # # generate token using customauth:
    # path('gettoken/',CustomAuthToken.as_view())
]

# teminal command here we need two terminal one is for server running other is for below command:
# http POST http://127.0.0.1:8000/gettoken/ username='nisha' password='geekyshow'