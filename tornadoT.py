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
        self.write('hah')

    def post(self, *args, **kwargs):
        self.write(self.get_cookie('gekaibin'))

class testHeader(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        result = yield executor.submit(TbUserInfo.select().where,TbUserInfo.ui_user == 1)
        # self.render('testheader.html',text="")
        # result = TbUserInfo.get(TbUserInfo.ui_user == 1) #同上一句查询
        # print(help(result))
        #cokkie是通过header(请求报头)传递参数过去  然后协议检测到之后就会增加一个键值对
        # self.set_header('Set-Cookie','gekaibin = zhangdemei;path=/') #这样也能设置cookie
        self.set_cookie('gekaibin','zhangdemei',expires=time.strptime('2017-09-14 12:00:00',"%Y-%m-%d %H:%M:%S"))
        print(result.first().ui_user_name)
        self.write(self.get_cookie('gekaibin'))
    # def set_default_headers(self):
    #     self.set_header('x-xss-protection',0)
    #     self.set_header('X-XSS-Protection',0)
#<script>alert("hhh")</script>
    def post(self, *args, **kwargs):
        text = self.get_argument('test')
        # self.set_header('x-xss-protection',0)
        # self.set_header('X-XSS-Protection',0)
        self.render('testheader.html',text=text)

class Application(web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        self.db = PooledMySQLDatabase(database='TORNADO',max_connections=20,timeout=60,host='127.0.0.1',user='root',password='g123567G')
            # torndb.Connection(host='127.0.0.1',database='TORNADO',user='root',password='g123567G')


if __name__ == '__main__':
    html_path = os.path.join(STATIC_PATH,'html')
    print(html_path)
    #autoescape : 关闭返回的数据被自动转义  ,autoescape=None 是全局的
    app = Application([(r'/testHeader',testHeader)
        ,(r'/(.*)',StaticFileHandler,{'path': html_path,'default_filename':'index.html'})
                           ],static_path=STATIC_PATH,debug=True,template_path=TEMPLATE_PATH)
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8000)
    ioloop.IOLoop.current().start()

    #git