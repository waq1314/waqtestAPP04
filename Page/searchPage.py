# 导包
from Base.base import Base
from Page.PageElements import PageElements

# 定义搜索页面元素
class SearchPage(Base):
    # 初始化 重写Base的init
    def __init__(self):
        super().__init__()
    # 编写业务方法
    # 输入搜索内容
    def search_text(self,text):
        self.send_ele(PageElements.search_input,text)
    # 获取搜索结果
    def get_search_results(self):
        results=self.search_eles(PageElements.search_results)
        return [i.text for i in results]
