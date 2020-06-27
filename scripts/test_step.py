import allure
class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("我是测试步骤名称")
    def test_001(self):
        """测试步骤"""
        allure.attach("我是描述的内容","附件名字")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_002(self):
        assert False