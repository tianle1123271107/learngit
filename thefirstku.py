from urllib import request
from urllib import error
import socket
# response=request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# 这里就用到urllib.parse，通过bytes(urllib.parse.urlencode())可以将post数据进行转换放到urllib.request.urlopen的data参数中。这样就完成了一次post请求。
# 所以如果我们添加data参数的时候就是以post请求方式请求，如果没有data参数就是get请求方式
from urllib import parse
try:
    aa=bytes(parse.urlencode({'word': 'hello','name':'tianle'}),encoding='utf8')  # parse.urlencode将字典的参数形式  变成josn的格式作为参数参入post
    print(aa)
    # timeout参数的使用
    # 在某些网络情况不好或者服务器端异常的情况会出现请求慢的情况，或者请求异常，所以这个时候我们需要给
    # 请求设置一个超时时间，而不是让程序一直在等待结果
    response=request.urlopen('http://httpbin.org/post',data=aa,timeout=0.01)
    print(response.read())
    # url='http://www.baidu.com'
    # print(parse.urlparse(url))   #  parse.urlparse(url)  解析url的基本构成 scheme='http', netloc='www.baidu.com', path='', params='', query='', fragment=''
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):  #urllib.error 异常处理模块  如果异常的原因是超时  那么打印超时
        print('time out')


