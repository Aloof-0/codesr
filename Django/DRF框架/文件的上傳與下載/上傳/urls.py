from  django.urls import path
from book import view
urlpatterns = [
    path('download_file/', view.UploadFile.as_view())
]