from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [  
    path('admin/', admin.site.urls),

    #local apps
    #authentication app links to the directory 
    path('api/', include('authentication.urls')),

    #articles app links to the directory 
    path('api/', include('articles.urls')),

    #profiles app links to the directory 
    path('api/', include('profiles.urls')),

    #recommender app links to the directory 
    path('api/', include('recommender.urls')),

    #addes rest apps  using djnago rest framwork 
    path("api-auth/", include("rest_framework.urls")),#login

    path("api/dj-rest-auth/", include("dj_rest_auth.urls")), #for log in : api/dj-rest-auth/login
    ]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#using : dj_rest_auth.urls :
# ---------------------------
# Login: /api/dj-rest-auth/login/
# Logout: /api/dj-rest-auth/logout/
# Password change: /api/dj-rest-auth/password/change/
# Password reset: /api/dj-rest-auth/password/reset/
# Password reset confirm: /api/dj-rest-auth/password/reset/confirm/
# User registration: /api/dj-rest-auth/registration/