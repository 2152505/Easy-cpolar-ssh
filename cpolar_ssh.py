#导入必要的库，如果没有对应的库，请使用pip install requests,pip install beautifulsoup4,pip install lxml进行安装
import requests
from bs4 import BeautifulSoup
import pyperclip
import configparser
import os
import time
def main():
    # 登陆Cpoalr官网
    # cpolar官网登陆界面的网址
    login_url = 'https://dashboard.cpolar.com/login'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    cfg_path=BASE_DIR+'/user.cfg'
    
    config_parser = configparser.ConfigParser()
    config_parser.read(cfg_path,encoding='utf-8')
    
    #print(cfg_path)
    
    config_login_original = config_parser.get('login','login')
    config_password_original = config_parser.get('login','password')
    config_user_original = config_parser.get('user','user')
    config_mode_original = config_parser.get('mode','mode')
    
    #print(config_login_original+"  "+config_password_original+"  "+config_user_original)
    # 读取配置文件中的账号和密码
    login=""
    password=""
    user=""
    mode=""
    for i in range(1,len(config_login_original)-1):
      login+=config_login_original[i]
    for i in range(1,len(config_password_original)-1):
      password+=config_password_original[i]
    for i in range(1,len(config_user_original)-1):
      user+=config_user_original[i]
    for i in range(1,len(config_mode_original)-1):
      mode+=config_mode_original[i]
    #print(login+"  "+password+"  "+user)
    # 去除账号和密码中的特殊字符
    #注意，此处有一个大坑，因为configparser读取的账号和密码中，会包含一些特殊字符，比如：‘ ,所以需要我们手动去除这些特殊字符
    login_data = {
      "login":login,
      #注意：此处做的很棒！！！要学会自己去分析，之前的代码一直无法真正得到隧道的数值，通过查看返回的页面新我们发现，实际上，浏览器需要带的参数名称出现了问题
      # 正确的参数名称应该是：login，而不是loginName，这也提醒了我们，一定要学会去分析，去search，而是一味地copy粘贴，这样只会让我们越来越懒，越来越不会思考
      "password":password
    }
    
    # 用户名和密码，请在这里修改成自己的账号和密码
    headers = {
    'Connection': 'close'
    }
    # 关闭长期链接，不然会报错
    session = requests.session()
    response = session.post(login_url, headers=headers,data=login_data)
    #发送访问请求
    # 进入status页面
    status_url = 'https://dashboard.cpolar.com/status'
    response = session.get(status_url)
    # 抓取页面
    
    from lxml import etree

    html=etree.HTML(response.text)
    # 解析html文件
    #print(response.text)
    xpath_result_1 = "/html/body/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/th/a"
    xpath_result_2 = "/html/body/div[5]/div/div[2]/div[2]/table/tbody/tr[2]/th/a"
    xpath_result_3 = "/html/body/div[5]/div/div[2]/div[2]/table/tbody/tr[3]/th/a"
    #非会员用户只有三个目标值
    
    tunnle_ip_1=html.xpath(xpath_result_1)[0]
    tunnle_ip_2=html.xpath(xpath_result_2)[0]
    tunnle_ip_3=html.xpath(xpath_result_3)[0]
    # print(tunnle_ip)
    # 获取tcp地址
    # 使用xpath获取对应的ssh地址
    # 最后如果不转码会是个 bytes 类型数据
    string_1 = etree.tostring(tunnle_ip_1, encoding='utf-8').decode('utf-8')     
    string_2 = etree.tostring(tunnle_ip_2, encoding='utf-8').decode('utf-8')     
    string_3 = etree.tostring(tunnle_ip_3, encoding='utf-8').decode('utf-8')     
    #print(string)
    import re 
    herf_content_1=re.split('<|>',string_1)
    herf_content_2=re.split('<|>',string_2)
    herf_content_3=re.split('<|>',string_3)
    #print(herf_content)
    
    tcp_ip=[]
    tcp_ip.append([tcp_index for tcp_index in herf_content_1 if "tcp" or "https" in tcp_index])
    tcp_ip.append([tcp_index for tcp_index in herf_content_2 if "tcp" or "https" in tcp_index])
    tcp_ip.append([tcp_index for tcp_index in herf_content_3 if "tcp" or "https" in tcp_index])
    
    #for i in range(3):
      #print(tcp_ip[i][2])
      
    #print(tcp_ip)
    print(mode)
    for i in range(3):
      if ("http" in tcp_ip[i][2]) and mode=="https":
        command="{https}".format(https=tcp_ip[i][2])
        break
        # print(command)
      else:
        #print(tcp_ip[i][2])
        #print(re.split(':|/',tcp_ip[i][2]))
        command = "ssh {user}@{tcp_ip_dns} -p {tcp_ip_port}".format(user=user,tcp_ip_dns=re.split(':|/',tcp_ip[i][2])[3],tcp_ip_port=re.split(':|/',tcp_ip[i][2])[4])
        break
    pyperclip.copy(command)
      
      
    print("================================================")
    print("Your login name is : {login}".format(login=login))
    print("Your user name is : {user}".format(user=user))
    print("Programme is successfully registered")
    print("================================================")
    print("The command is copied to your clipboard")
    print("================================================")
    time.sleep(30)
    
if __name__ == "__main__":
    main()


