"""
# 启动运行 初始化：
init2 被调用
init1 被调用
init2 被调用
init1 被调用
第一次请求开始：
before request1 被调用
before request2 被调用
装饰器被调用了
请求的方法：GET
装饰器被调用了
请求的方法：GET
after response2 被调用
after response1 被调用

# 第二次请求 只有内部
before request1 被调用
before request2 被调用
装饰器被调用了
请求的方法：GET
装饰器被调用了
请求的方法：GET
after response2 被调用
after response1 被调用
"""


# 请求自上而下 响应自下而上
def my_middleware1(get_response):

    print('init1 被调用')

    def middleware(request):

        print('before request1 被调用')

        response = get_response(request)

        print('after response1 被调用')

        return response

    return middleware


def my_middleware2(get_response):

    print('init2 被调用')

    def middleware(request):

        print('before request2 被调用')

        response = get_response(request)

        print('after response2 被调用')

        return response

    return middleware

