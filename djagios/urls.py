from django.urls import path
from django.contrib import admin
from data_collector.views import StatusView, AlertListView, NewAlertView, EditAlertView, DeleteAlertView, RecordDataApiView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StatusView.as_view(), name='status'),
    path('alerts/', AlertListView.as_view(), name='alerts-list'),
    path('alerts/new/', NewAlertView.as_view(), name='alerts-new'),
    path('alerts/<int:pk>/edit/', EditAlertView.as_view(), name='alerts-edit'),
    path('alerts/<int:pk>/delete/',
         DeleteAlertView.as_view(), name='alerts-delete'),
    path('record/', csrf_exempt(RecordDataApiView.as_view()), name='record-data'),
]
