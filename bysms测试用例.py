from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
wd = webdriver.Chrome()
wd.get('http://127.0.0.1/mgr/sign.html')

#1.输入用户名和密码
user = wd.find_element(By.ID, 'username')
password = wd.find_element(By.ID, 'password')
user.send_keys('byhy')
password.send_keys('88888888\n')

#2.进入操作页面
time.sleep(1)
wd.get('http://127.0.0.1/mgr/#/')
#保存当前网页

#

#UI-0101找到客户、药品、菜单
elements_menu = wd.find_elements(By.CSS_SELECTOR, ".sidebar-menu.tree > li:nth-child(-n+4) span")
#3.1打印出结果
for element in elements_menu:
    print(element.text)


#UI-0102输入客户名为 南京中医院 的客户
#点击添加客户按钮
tianjia = wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md')
tianjia.click()

time.sleep(1)
#填入信息
element_ShuRu = wd.find_elements(By.CSS_SELECTOR, '.form-control')
element_ShuRu[0].send_keys('南京中医院')
element_ShuRu[1].send_keys('025522766')
element_ShuRu[2].send_keys('江苏省南京市秦淮区大明路157号')
#点击创建按钮
ChuangJian = wd.find_elements(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs')
ChuangJian[0].click()#点击创建
ChuangJian[1].click()#点击取消

time.sleep(1)


#UI-0103修改客户名为：南京省中医院
#点击编辑按钮
Bianji = wd.find_element(By.CSS_SELECTOR, '.btn-green.btn-outlined.btn-xs')
Bianji.click()
#修改客户名
Set_username = wd.find_elements(By.CSS_SELECTOR, '.form-control')
Set_username[1].clear()
Set_username[1].send_keys('南京省中医院')


# UI-0105
# 3.点击菜单药品
Yaoping = wd.find_element(By.CSS_SELECTOR, '[href="#/medicines"]')
Yaoping.click()
#3.1点击添加药品
time.sleep(1)
Yaoping_tianjia = wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md')
Yaoping_tianjia.click()
time.sleep(1)
#3.2填入药品信息
Yaoping_xinxi = wd.find_elements(By.CSS_SELECTOR, '.form-control')
Yaoping_xinxi [0].send_keys('六味地黄丸')
Yaoping_xinxi [1].send_keys('SLE34234234')
Yaoping_xinxi [2].send_keys('六味地黄丸，中成药名。为补益剂，具有滋阴补肾之功效。用于肾阴亏损，头晕耳鸣，腰膝酸软，骨蒸潮热，盗汗遗精，消渴。')
#点击创建按钮
ChuangJian = wd.find_elements(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs')
ChuangJian[0].click()#点击创建
ChuangJian[1].click()#点击取消


#UI-0106
#点击跳转值白月黑羽官网
TiaoZhuan = wd.find_element(By.CSS_SELECTOR, '[href="http://www.byhy.net"]')
TiaoZhuan.click()
#保存当前网页
mainwindow = wd.current_window_handle

for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if "白月黑羽" in wd.title:
        break
#跳转到白月黑羽(selenium层面)
wd.switch_to.window(handle)
#窗口最大化
wd.maximize_window()
time.sleep(1)
#获取官网页眉
YeMei = wd.find_elements(By.CSS_SELECTOR, '.nav-link ')
for YeMeis in YeMei:
    print(YeMeis.text)
#回到销售管理系统
wd.switch_to.window(mainwindow)
#点击右侧管理员头像
RightPhoto = wd.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')
RightPhoto[1].click()
time.sleep(1)
#点击退出登录
Exit = wd.find_element(By.CSS_SELECTOR, '.pull-right')
Exit.click()

if wd.current_url == "http://127.0.0.1/mgr/sign.html":
    print('成功退出登录')


# UI-0107
# 3.点击菜单药品
Yaoping = wd.find_element(By.CSS_SELECTOR, '[href="#/medicines"]')
Yaoping.click()
#3.1点击添加药品
time.sleep(1)
Yaoping_tianjia = wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md')
Yaoping_tianjia.click()
time.sleep(1)
#定位创建按钮
ChuangJian = wd.find_elements(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs')
#3.2填入药品信息
Yaoping_xinxi = wd.find_elements(By.CSS_SELECTOR, '.form-control')
Yaoping_xinxi [0].send_keys('青霉素盒装1')
Yaoping_xinxi [1].send_keys('YP-32342341')
Yaoping_xinxi [2].send_keys('青霉素注射液，每支15ml，20支装')
ChuangJian[0].click()#点击创建
time.sleep(2)
Yaoping_xinxi = wd.find_elements(By.CSS_SELECTOR, '.form-control')
Yaoping_xinxi [0].send_keys('青霉素盒装2')
Yaoping_xinxi [1].send_keys('YP-32342342')
Yaoping_xinxi [2].send_keys('青霉素注射液，每支15ml，20支装')
ChuangJian[0].click()#点击创建
time.sleep(2)
Yaoping_xinxi = wd.find_elements(By.CSS_SELECTOR, '.form-control')
Yaoping_xinxi [0].send_keys('青霉素盒装3')
Yaoping_xinxi [1].send_keys('YP-32342343')
Yaoping_xinxi [2].send_keys('青霉素注射液，每支15ml，20支装')
ChuangJian[0].click()#点击创建
ChuangJian[1].click()#点击取消
time.sleep(1)

#点击左侧菜单中的“客户”
LeftKeHu = wd.find_elements(By.CSS_SELECTOR,'.sidebar-menu.tree a')
LeftKeHu[0].click()

time.sleep(2)
#--------------------------------------------
#点击添加客户按钮
tianjia = wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md')
tianjia.click()
#定位创建按钮
ChuangJian = wd.find_elements(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs')
#添加客户
element_ShuRu = wd.find_elements(By.CSS_SELECTOR, '.form-control')
element_ShuRu[0].send_keys('南京中医院1')
element_ShuRu[1].send_keys('2551867851')
element_ShuRu[2].send_keys('江苏省-南京市-秦淮区-汉中路-501')
ChuangJian[0].click()#点击创建
time.sleep(1)
element_ShuRu = wd.find_elements(By.CSS_SELECTOR, '.form-control')
element_ShuRu[0].send_keys('南京中医院2')
element_ShuRu[1].send_keys('2551867852')
element_ShuRu[2].send_keys('江苏省-南京市-秦淮区-汉中路-502')
ChuangJian[0].click()#点击创建
time.sleep(1)
element_ShuRu = wd.find_elements(By.CSS_SELECTOR, '.form-control')
element_ShuRu[0].send_keys('南京中医院3')
element_ShuRu[1].send_keys('2551867853')
element_ShuRu[2].send_keys('江苏省-南京市-秦淮区-汉中路-503')
ChuangJian[0].click()#点击创建

#--------------------------------------------
#点击左侧菜单中的“订单”
DingDang = wd.find_elements(By.CSS_SELECTOR,'.sidebar-menu.tree a')
DingDang[2].click()
time.sleep(2)
#点击添加订单
tianjia_Dingdan = wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md')
tianjia_Dingdan.click()
#订单名称
DingDang_Name = wd.find_elements(By.CSS_SELECTOR, '.form-control')
DingDang_Name [0].send_keys('测试订单')
#客户名
KeHu_name = Select(wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(2) .xxx'))
KeHu_name.select_by_visible_text('南京中医院2')
#药品名称
YaoPing_name = Select(wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(3) .xxx'))
YaoPing_name.select_by_visible_text('青霉素盒装1')
#药品数量
YaoPing_Num = wd.find_element(By.CSS_SELECTOR,'.col-lg-8 [type="number"]')
YaoPing_Num.send_keys('100')
ChuangJian = wd.find_elements(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs')
ChuangJian[0].click()#点击创建

time.sleep(3100)