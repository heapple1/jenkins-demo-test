import time

def test_login_success():
    print("模拟登录成功")
    assert 1 + 1 == 2

def test_login_fail():
    time.sleep(1)
    print("模拟登录失败，故意断言失败")
    assert 1 + 1 == 3 # 故意写错，测试流水线报错