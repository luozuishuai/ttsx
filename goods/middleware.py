from django.http import HttpResponse
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        print('__init__')

    def process_request(self, request):
        print('生成请求对象后，路由匹配之前')
        print('request')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print('路由匹配后，视图函数调用之前')
        print('view')

    def process_response(self, request, response):
        print('视图函数执行后，响应内容返回浏览器之前')
        print('response')
        return response

    def process_exception(self, request, exception):
        print('发生异常:')
        print(exception)
        return HttpResponse('WHAT\'S THE FUCK')
