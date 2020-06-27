# 导包
from Base.base import Base
from Page.PageElements import PageElements
# 创建设置页面元素类，继承Base

class SettingPage(Base):
    # 初始化 重写Base的init
    def __init__(self):
        super().__init__()
    # 编写业务方法
    # 点击搜索按钮
    def click_search_btn(self):
        self.click_ele(PageElements.search_btn)
