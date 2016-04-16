# coding=utf-8

# 从标准库的"string"模块导入"Template" 类.它支持简单的字符串替换模板
from string import Template

# 用来创建一个CGI "Content-type:" 行, 参数缺省值为"text/html"
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

# 用在HTML页面最前端的标题中,页面本身储存在一个单独的文件templates/header.html
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
# 创建HTML页面尾部,参数用来动态的创建一组HTML链接标记,参数为一个字典
def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'# 字符串中加入空格的一种强制做法
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

# 返回表单最前面的HTML,允许调用者指定URL(表单数据将发送到这个URL),还可以指定GET or POST
def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

# 返回表单末尾的HTML,同时还允许调用者制定表单"submit"按钮的文本
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

# 给定一个单选钮的名和值,创建一个HTML单选钮
def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

# 给定一个列表,转换成HTML的无序列表
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

# 创建并返回一个HTML标题标记,默认2级标题
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

# 用HTML段落标记保卫一个文本段(一个字符串)
def para(para_text):
    return('<p>' + para_text + '</p>') 
