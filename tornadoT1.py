#coding = utf-8
from tornado import web,ioloop,httpserver,options
import json
import os
from tornado.web import StaticFileHandler,url,RequestHandler
from settings import *
from playhouse.pool import PooledMySQLDatabase
from tornado_models import *
from  tornado import gen,concurrent
import time
import base64, uuid
#拼接static文件路径

executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

class MainHandle(RequestHandler):

    # def initialize(self):
    #     """ 预处理方法 在set_deafuat_header方法之后调用 """
    #     if self.request.headers.get('Conrent-Type','').startswith('application/json'):
    #         self.json_args = json.loads(self.request.body)
    #
    # def prepare(self):
    #     """ 准备工作  在initialize之后调用 """
    #     pass
    #
    # def set_default_headers(self):
    #     """最先调用此方法 后面是initialize 当主动抛出错误的时候会再次调用此方法 会重置headers的设置  """
    #     pass
    #
    # def on_finish(self):
    #     """当请求完成 数据真正的传输过去的时候调用"""
    #     pass
    #
    # def write_error(self, status_code, **kwargs):
    #     """ 当主动抛出错误时  先调用set_deafault_header方法 再调用此方法"""
    #     pass

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        # self.write(self.get_cookie('gekaibin'))
        pass

class testHeader(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        self.xsrf_token #可以直接获取到前端的Token值 如果没有会生成一个并设置到浏览器中
        # result = yield executor.submit(TbUserInfo.select().where,TbUserInfo.ui_user == 1)
        self.render('testheader.html')

    @gen.coroutine
    def post(self, *args, **kwargs):
        print(self.request.headers)
        self.write('post')


class Application(web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        #使用线程池连接mysql数据库
        self.db = PooledMySQLDatabase(
                database='TORNADO',
                max_connections=20,timeout=60,
                host='127.0.0.1',
                user='root',
                password='g123567G'
        )


if __name__ == '__main__':
    html_path = os.path.join(STATIC_PATH,'html')
    print(html_path)
    settings = dict(
            static_path=STATIC_PATH,
            debug=True,
            xsrf_cookies = True,
            template_path=TEMPLATE_PATH,
            cookie_secret='PQvw9USaSwWuPNrs6m6x/MsurHFz6UjGrqOXeK4GAoU=',
    )
    #autoescape : 关闭返回的数据被自动转义  ,autoescape=None 是全局的
    app = Application([(r'/testHeader',testHeader),
        (r'/(.*)',StaticFileHandler,{'path': html_path,'default_filename':'index.html'})
                           ],**settings)
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8887)
    ioloop.IOLoop.current().start()
