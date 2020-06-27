# 定义封装页面所有元素的类
from selenium.webdriver.common.by import By

class PageElements():
    """管理所有页面的所有元素"""
    # ---设置页面元素---
    # 搜索按钮
    search_btn=(By.ID,"com.android.settings:id/search")

    # ---搜索页面元素---
    # 输入框
    search_input=(By.ID,"android:id/search_src_text")
    # 搜索结果
    search_results=(By.ID,"com.android.settings:id/title")