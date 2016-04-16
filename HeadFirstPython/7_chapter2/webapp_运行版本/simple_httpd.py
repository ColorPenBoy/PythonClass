### 用Python构建一个Web服务器必须有下面这5行代码 ###

# 导入Http服务器和CGI模块
from http.server import HTTPServer, CGIHTTPRequestHandler

# 指定一个端口
port = 8080

# 创建一个HTTP服务器
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)

# 显示一个友好消息
print("Starting simple_httpd on port: " + str(httpd.server_port))

# 启动服务器
httpd.serve_forever()
