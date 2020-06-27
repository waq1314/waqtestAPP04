# 导包
from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver

# 定义base类
class Base:
    # 初始化driver
    def __init__(self):
        self.driver = Driver.get_drvier()

    # 定义单个元素的定位方法
    def search_ele(self, loc, timeout=5, poll=1.0):
        # 利用显示等待定位元素
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 定义多个元素的定位方法
    def search_eles(self, loc, timeout=5, poll=1.0):
        # 利用显示等待定位元素
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))
    # 定义点击的方法
    def click_ele(self, loc, timeout=5, poll=1.0):
        self.search_ele(loc,timeout,poll).click()
    # 定义输入方法
    def send_ele(self,loc,text,timeout=5,poll=1.0):
        input_text=self.search_ele(loc,timeout,poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)