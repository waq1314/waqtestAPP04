# 封装一个类，返回页面的实例化对象
from Page.searchPage import SearchPage
from Page.settingPage import SettingPage

class Page:
    # 返回设置页面实例化对象
    @classmethod
    def get_settingPage(cls):
        return SettingPage()
    # 返回搜索页面实例化对象
    @classmethod
    def get_searchPage(cls):
        return SearchPage()