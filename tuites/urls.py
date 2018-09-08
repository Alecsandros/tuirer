from django.urls import path
from tuites.views import PostTuiteView, LikeTuiteView, SingleTuiteView, ListTuiteView


app_name = 'tuites'

urlpatterns = [
    path('postar/', PostTuiteView.as_view(), name='post_tuite'),
    path('tuites', ListTuiteView.as_view(), name='home'),
    path('tuite/<int:pk>', SingleTuiteView.as_view(), name='tuite'),

    # Actions
    path('tuite/<int:pk>/like', LikeTuiteView.as_view(), name='like'),
]
