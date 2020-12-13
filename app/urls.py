# appのurls.pyはデフォルトで設定されていないので、手動で追加
from django.urls import path
from .views import CallbackView

# urlpatternsの中にルーティングを設定
urlpatterns = [
    # callbackにアクセスがあった場合、views.pyファイルのCallbackViewクラスにアクセスするようにする
    path('callback/', CallbackView.as_view(), name='callback')
]