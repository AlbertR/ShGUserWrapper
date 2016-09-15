from login_ui import Ui_Login

class LoginWindowSlots(Ui_Login):

	def Login(self):
		login = self.LoginEdit.text() # Get login
		password = self.PasswordEdit.text() # Get password

		print(login)
		print(password)

		return None
