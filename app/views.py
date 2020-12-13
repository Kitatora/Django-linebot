from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse

# callbackにアクセスがあった場合、OKを返すようにする。文字列を返すだけなら、templateを介さずとも、HttpResponseだけでOK
class CallbackView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')
# Create your views here.
