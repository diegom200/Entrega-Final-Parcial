from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from logapp import views

urlpatterns = [
    path("crear/", views.SignUpView.as_view(), name ="logapp_signup"),
    path("profile/<pk>/", views.LogappProfile.as_view(), name ="logapp_profile"),
    path("editar/<pk>/", views.LogappUpdate.as_view(), name ="logapp_edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)