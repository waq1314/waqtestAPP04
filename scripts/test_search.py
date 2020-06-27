# 导包
import pytest

from Base.driver import Driver
from Base.page import Page
# 定义测试类,以Teat开头
class Test_Search:

    # 退出driver
    def teardown_class(self):
      Driver.quit_driver()
    # 定义测试方法,以test开头
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        Page.get_settingPage().click_search_btn()
    # 参数化
    @pytest.mark.parametrize("search_data,exp_data",[("1","休眠"),("i","IP地址"),("m","MAC地址")])
    def test_search(self,search_data,exp_data):

        # 点击搜索输入框
        Page.get_searchPage().search_text(search_data)
        # 断言
        assert exp_data in Page.get_searchPage().get_search_results()
