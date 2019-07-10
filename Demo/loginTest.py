
class login():
    def __init__(self,driver):
        self.driver = driver
    def findUserName(self):
        try:
            user = self.driver.find_element_by_id('txtUserName')
            return user
        except Exception as e:
            print('无法找到user enter')
            print('e')
    def findPassWord(self):
        try:
            ps = self.driver.find_element_by_id('txtPassword')
            return ps
        except Exception as e:
            print('无找到password enter')
            print(e)
    def findLoginButtun(self):
        try:
            lb = self.driver.find_element_by_id('btnLogin')
            return lb
        except Exception as e:
            print('无法找到login buttun')
            print(e)

    def submit(self,user,password):
        self.findUserName().send_keys(user)
        self.findPassWord().send_keys(password)
        self.findLoginButtun().click()

    def cls(self):
        self.findUserName().clear()
        self.findPassWord().clear()
