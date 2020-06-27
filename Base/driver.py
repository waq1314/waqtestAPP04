# 导包
from appium import webdriver

# 创建driver类
class Driver:
    app_driver = None

    # 声明driver的方法
    @classmethod
    def get_drvier(cls):
        if not cls.app_driver:
            # server 启动参数
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            # 声明我们的driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.app_driver
        else:
            return cls.app_driver

    # 退出driver的方法
    @classmethod
    def quit_driver(cls):
        # driver有值退出
        if cls.app_driver:
            cls.app_driver.quit()
            # 重置driver为空
            cls.app_driver = None
