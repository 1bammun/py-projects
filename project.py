from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMessageBox
import sys
import mysql.connector

class connection():
    def connect(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "STAFF")
        mycusor = mydb.cursor()
        return mycusor

class Admin(QtWidgets.QMainWindow):
    fname = []
    lname = ""
    email = ""
    courses = []

    def __init__(self, parent=None):
        super(Admin, self).__init__(parent)
        uic.loadUi("admin.ui", self)

        self.back = self.findChild(QtWidgets.QPushButton, 'back_admin')
        self.back.clicked.connect(self.go_back)
        # self.front = self.findChild(QtWidgets.QPushButton, 'profile_admin')
        # self.front.clicked.connect(self.go_profile)
        # self.front = self.findChild(QtWidgets.QPushButton, 'leaves_admin')
        # self.front.clicked.connect(self.go_leaves)
        # self.time_table = self.findChild(QtWidgets.QPushButton, 'schedule_admin')
        # self.time_table.clicked.connect(self.go_schedule)
        # self.front = self.findChild(QtWidgets.QPushButton, 'settings_admin')
        # self.front.clicked.connect(self.go_settings)

        self.fname_ad = self.findChild(QtWidgets.QLabel, "fname_admin1")
        self.lname_ad = self.findChild(QtWidgets.QLabel, "lname_admin1")
        self.email_ad = self.findChild(QtWidgets.QLabel, "email_admin1")
        self.courses_ad = self.findChild(QtWidgets.QLabel, "course_admin1")
        self.show()

    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()
    # def go_profile(self):
    #     self.hide()
    #     menu = Profile(self)
    #     menu.show()
    # def go_leaves(self):
    #     self.hide()
    #     menu = Leave(self)
    #     menu.show()
    # def go_schedule(self):
    #     self.hide()
    #     menu = Schedule(self)
    #     menu.show()
    # def go_settings(self):
    #     self.hide()
    #     menu = Setting(self)
    #     menu.show()

    def setValues(self):
        self.fname_ad.setText(self.fname)
        self.lname_ad.setText(self.lname)
        self.email_ad.setText(self.email)
        self.courses_ad.setText(self.courses)
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="staff_mgt_system")
            mycusor = mydb.cursor()
            sql = "select * from staff where emp_id=(emp_id[0:])"
            Values = (self.email_ad.text())
            mycusor.execute(sql, Values)
            result = mycusor.fetchone()
            if result == None:
                msgBox.setText("Email Address Not Found")
                msgBox.exec_()
            else:
                self.window().close()
                reg = Admin(self)
                reg.fname = result[1]
                reg.lname = result[2]
                reg.email = result[3]
                reg.courses = result[8]
                reg.setValues()

        except Exception as error:
            print('An Error Occurred', error)

class Admin_Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Admin_Login, self).__init__(parent)
        uic.loadUi('admin_log.ui', self)

        self.username = self.findChild(QtWidgets.QLineEdit, 'username_admin_log')
        self.password = self.findChild(QtWidgets.QLineEdit, 'password_admin_log')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.back = self.findChild(QtWidgets.QPushButton, 'back_admin_log')
        self.back.clicked.connect(self.go_back)
        self.submit = self.findChild(QtWidgets.QPushButton, 'submit_admin_log')
        self.submit.clicked.connect(self.do_login)
        self.show()

    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()

    def do_login(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            if self.username.text() == "":
                msgBox.setText("Please Fill Your Username")
                msgBox.exec_()
            elif self.password.text() == "":
                msgBox.setText("Password cannot be empty")
                msgBox.exec_()
            elif len(self.password.text()) < 4:
                msgBox.setText("Password cannot be less than four digits")
                msgBox.exec_()
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="staff_mgt_system")
            mycusor = mydb.cursor()
            sql = "select * From admin where username=%s password=%s"
            Values = (self.username.text(), self.password.text())
            mycusor.execute(sql, Values)
            result = mycusor.fetchone()
            if result == None:
                msgBox.setText("Admin Account Does Not Exist!!!")
                msgBox.exec_()
            else:
                self.window().close()
                reg = Admin(self)
                # reg.fname = result[1]
                # reg.lname = result[2]
                # reg.email = result[3]
                # reg.courses = result[8]
                # reg.setValues()
                reg.show()


        except Exception as error:
                print('An Error Occurred', error)


class Schedule(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Schedule, self).__init__(parent)
        uic.loadUi('time_table.ui', self)
        self.back = self.findChild(QtWidgets.QPushButton, 'back_schedule')
        self.back.clicked.connect(self.go_back)
        self.show()

    def go_back(self):
        self.hide()
        menu = Profile(self)
        menu.show()


class Forgot_Password(QtWidgets.QMainWindow):
    def __init__(self, parent=None):

        super(Forgot_Password, self).__init__(parent)
        uic.loadUi('reset.ui', self)

        self.email = self.findChild(QtWidgets.QLineEdit, 'email_reset_password')
        self.password = self.findChild(QtWidgets.QLineEdit, 'pword_reset_password')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.back = self.findChild(QtWidgets.QPushButton, 'back_reset')
        self.back.clicked.connect(self.go_back)
        self.submit = self.findChild(QtWidgets.QPushButton, 'submit_reset_password')
        self.submit.clicked.connect(self.do_reset)
        self.show()

    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()

    def do_reset(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            if self.email.text() == "":
                msgBox.setText("Please Enter The Email You Registered With !")
                msgBox.exec_()
            elif self.password.text() == "":
                msgBox.setText("Please Enter New Password!")
                msgBox.exec_()
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="staff_mgt_system")
                mycusor = mydb.cursor()
                sql = "Update Staff SET Password=%s WHERE email=%s"
                Values = (self.password.text(), self.email.text())
                mycusor.execute(sql, Values)
                mydb.commit()
                msgBox.setText("Password Reset Successful!!")
                msgBox.exec_()
        except Exception as error:
            print('An Error Occurred', error)

class Leave(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Leave, self).__init__(parent)
        uic.loadUi('apply.ui', self)

        self.emp_id_leave = self.findChild(QtWidgets.QLineEdit, 'emp_id_leave')
        self.leave = self.findChild(QtWidgets.QComboBox, 'leave_type')
        self.from_date = self.findChild(QtWidgets.QDateEdit, 'from_date')
        self.to_date = self.findChild(QtWidgets.QDateEdit, 'to_date')
        self.reason = self.findChild(QtWidgets.QTextEdit, 'reason')

        self.back = self.findChild(QtWidgets.QPushButton, 'back_leave')
        self.back.clicked.connect(self.go_back)

        self.front = self.findChild(QtWidgets.QPushButton, 'profile_leave')
        self.front.clicked.connect(self.go_profile)
        self.front = self.findChild(QtWidgets.QPushButton, 'settings_leave')
        self.front.clicked.connect(self.go_settings)
        self.time_table = self.findChild(QtWidgets.QPushButton, 'schedule_leave')
        self.time_table.clicked.connect(self.go_time_table)

        self.reset_button = self.findChild(QtWidgets.QPushButton, 'reset_leave')
        self.reset_button.clicked.connect(self.emp_id_leave.clear)
        self.reset_button.clicked.connect(self.leave.clear)
        self.reset_button.clicked.connect(self.from_date.clear)
        self.reset_button.clicked.connect(self.to_date.clear)
        self.reset_button.clicked.connect(self.reason.clear)

        self.apply_button = self.findChild(QtWidgets.QPushButton, 'apply_leave')
        self.apply_button.clicked.connect(self.do_apply)
        self.show()

    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()
    def go_time_table(self):
        self.hide()
        menu = Schedule(self)
        menu.show()
    def go_profile(self):
        self.hide()
        menu = Profile(self)
        menu.show()
    def go_settings(self):
        self.hide()
        menu = Setting(self)
        menu.show()

    def do_apply(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            if self.emp_id_leave.text() == "":
                msgBox.setText("Please Enter Your Identification Number!")
                msgBox.exec_()
            elif self.leave_type.currentText() == "-Select-":
                msgBox.setText("Please Select Leave Type!")
                msgBox.exec_()
            # elif self.from_date.DateTime() == "-Select-":
            #     msgBox.setText("Please Enter Start Date!")
            #     msgBox.exec_()
            # elif self.to_date.DateTime() == "-Select-":
            #     msgBox.setText("Please Enter End Date!")
            #     msgBox.exec_()
            elif self.reason.setText(self, str) == "":
                msgBox.setText("Please Fill In Your Reason For Leave!")
                msgBox.exec_()
            else:
                Window.close()
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="staff_mgt_system")
                mycusor = mydb.cursor()
                sql = "Insert Into Apply_Leave(Emp_Id, Leave_Type, Reason) " \
                      "Values(%s,%s,%s)"
                Values = (
                self.emp_id_leave.num(), self.leave.text(), self.reason.setText(self, str))
                mycusor.executestr((sql, Values))
                mydb.commit()
                msgBox.setText("Record Inserted Successfully!!")
                msgBox.exec_()
        except Exception as error:
            print('An Error Occurred', error)

class Profile(QtWidgets.QMainWindow):
    emp_id = ""
    fname = []
    lname = ""
    email = []
    phone_number = ""
    gender = ""
    address = ""
    state = ""
    courses = []
    username = ""
    def __init__(self, parent=None):
        super(Profile, self).__init__(parent)
        uic.loadUi("profile.ui", self)

        self.back = self.findChild(QtWidgets.QPushButton, 'back_profile')
        self.back.clicked.connect(self.go_back)
        self.front = self.findChild(QtWidgets.QPushButton, 'leaves_profile')
        self.front.clicked.connect(self.go_leaves)
        self.front = self.findChild(QtWidgets.QPushButton, 'settings_profile')
        self.front.clicked.connect(self.go_settings)
        self.time_table = self.findChild(QtWidgets.QPushButton, 'schedule_profile')
        self.time_table.clicked.connect(self.go_time_table)


        self.search_button = self.findChild(QtWidgets.QPushButton, 'search_profile')
        self.search_button.clicked.connect(self.do_search)
        self.email_search_prof = self.findChild(QtWidgets.QLineEdit, 'email_search_profile')

        self.time_table = self.findChild(QtWidgets.QPushButton, 'time_table_profile')
        self.time_table.clicked.connect(self.go_time_table)

        self.emp_id_prof = self.findChild(QtWidgets.QLabel, "emp_id_profile")
        self.fname_prof = self.findChild(QtWidgets.QLabel, "fname_profile")
        self.lname_prof = self.findChild(QtWidgets.QLabel, "lname_profile")
        self.email_prof = self.findChild(QtWidgets.QLabel, "email_profile")
        self.phone_number_prof = self.findChild(QtWidgets.QLabel, "phone_number_profile")
        self.gender_prof = self.findChild(QtWidgets.QLabel, "gender_profile")
        self.address_prof = self.findChild(QtWidgets.QLabel, "address_profile")
        self.state_prof = self.findChild(QtWidgets.QLabel, "state_profile")
        self.courses_prof = self.findChild(QtWidgets.QLabel, "course_profile")
        self.username_prof = self.findChild(QtWidgets.QLabel, "username_profile")
        self.show()
    def go_time_table(self):
        self.hide()
        menu = Schedule(self)
        menu.show()
    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()
    def go_leaves(self):
        self.hide()
        menu = Leave(self)
        menu.show()
    def go_settings(self):
        self.hide()
        menu = Setting(self)
        menu.show()

    def setValues(self):
        self.emp_id_prof.setNum(self.emp_id)
        self.fname_prof.setText(self.fname)
        self.lname_prof.setText(self.lname)
        self.email_prof.setText(self.email)
        self.phone_number_prof.setText(self.phone_number)
        self.gender_prof.setText(self.gender)
        self.address_prof.setText(self.address)
        self.state_prof.setText(self.state)
        self.courses_prof.setText(self.courses)
        self.username_prof.setText(self.username)
    def do_search(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="staff_mgt_system")
            mycusor = mydb.cursor()
            sql = "select * from staff where email=%s"
            values = (self.email_search_prof.text())
            mycusor.execute(sql, (values,))
            result = mycusor.fetchone()
            if result == None:
                msgBox.setText("Email Address Not Found")
                msgBox.exec_()
            else:
                self.window().close()
                reg = Profile(self)
                reg.emp_id = result[0]
                reg.fname = result[1]
                reg.lname = result[2]
                reg.email = result[3]
                reg.phone_number = result[4]
                reg.gender = result[5]
                reg.address = result[6]
                reg.state = result[7]
                reg.courses = result[8]
                reg.setValues()

        except Exception as error:
                print('An Error Occurred', error)

class Staff(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Staff, self).__init__(parent)
        uic.loadUi("staff.ui", self)
        self.username = self.findChild(QtWidgets.QLineEdit, "username")
        self.password = self.findChild(QtWidgets.QLineEdit, "password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signin = self.findChild(QtWidgets.QPushButton, 'signin_staff')
        self.signin.clicked.connect(self.sign_in)
        self.signup = self.findChild(QtWidgets.QPushButton, 'signup_staff')
        self.signup.clicked.connect(self.sign_up)
        self.signup = self.findChild(QtWidgets.QPushButton, 'signup_staff2')
        self.signup.clicked.connect(self.sign_up)
        self.signin = self.findChild(QtWidgets.QPushButton, 'email_signin')
        self.signin.clicked.connect(self.email_sign_in)
        self.signin = self.findChild(QtWidgets.QPushButton, 'email_signin2')
        self.signin.clicked.connect(self.email_sign_in)
        self.signup = self.findChild(QtWidgets.QPushButton, 'forgot')
        self.signup.clicked.connect(self.forgot_sign_in)

        self.signin_admin = self.findChild(QtWidgets.QPushButton, 'admin_staff')
        self.signin_admin.clicked.connect(self.admin_sign_in)
        self.show()
    def email_sign_in(self):
        Window.close()
        reg = Use_email(self)
        reg.show()
    def forgot_sign_in(self):
        Window.close()
        reg = Forgot_Password(self)
        reg.show()
    def sign_up(self):
        Window.close()
        reg = Reg(self)
        reg.show()
    def admin_sign_in(self):
        Window.close()
        reg = Admin_Login(self)
        reg.show()
    def sign_in(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            if self.username.text() == "":
                msgBox.setText("Please Fill Your Username")
                msgBox.exec_()
            elif self.password.text() == "":
                msgBox.setText("Password cannot be empty")
                msgBox.exec_()
            elif len(self.password.text()) < 4:
                msgBox.setText("Password cannot be less than four")
                msgBox.exec_()
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="staff_mgt_system")
            mycusor = mydb.cursor()
            sql = "select * from staff where username=%s and password=%s"
            values = (self.username.text(), self.password.text())
            mycusor.execute(sql, values)
            result = mycusor.fetchone()
            if result == None:
                msgBox.setText("Invalid Login Details")
                msgBox.exec_()
            else:
                self.window().close()
                reg = Profile(self)
                reg.emp_id = result[0]
                reg.fname = result[1]
                reg.lname = result[2]
                reg.email = result[3]
                reg.phone_number = result[4]
                reg.gender = result[5]
                reg.address = result[6]
                reg.state = result[7]
                reg.courses = result[8]
                reg.username = result[9]
                reg.setValues()
                reg.show()

        except Exception as error:
            print(error)

class Use_email(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Use_email, self).__init__(parent)
        uic.loadUi("email_signin.ui", self)
        self.signin = self.findChild(QtWidgets.QPushButton, 'email_signin_button')
        self.signin.clicked.connect(self.sign_in)
        self.email = self.findChild(QtWidgets.QLineEdit, "email_signin")
        self.password = self.findChild(QtWidgets.QLineEdit, "password_email_signin")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back = self.findChild(QtWidgets.QPushButton, 'back_email_signin')
        self.back.clicked.connect(self.go_back)
        self.show()

    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()

    def sign_in(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            if self.email.text() == "":
                msgBox.setText("Please Fill Your Email Address")
                msgBox.exec_()
            elif self.password.text() == "":
                msgBox.setText("Password cannot be empty")
                msgBox.exec_()
            elif len(self.password.text()) < 4:
                msgBox.setText("Password cannot be less than four digits")
                msgBox.exec_()
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="staff_mgt_system")
            mycusor = mydb.cursor()
            sql = "select * from staff where email=%s and password=%s"
            values = (self.email.text(), self.password.text())
            mycusor.execute(sql, values)
            result = mycusor.fetchone()
            if result == None:
                msgBox.setText("Invalid Login Details")
                msgBox.exec_()
            else:
                self.window().close()
                reg = Profile(self)
                reg.emp_id = result[0]
                reg.fname = result[1]
                reg.lname = result[2]
                reg.email = result[3]
                reg.phone_number = result[4]
                reg.gender = result[5]
                reg.address = result[6]
                reg.state = result[7]
                reg.courses = result[8]
                reg.username = result[9]
                reg.setValues()
                reg.show()

        except Exception as error:
            print(error)

class Reg(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Reg, self).__init__(parent)
        uic.loadUi('signup.ui', self)

        self.lname = self.findChild(QtWidgets.QLineEdit, 'lname_signup')
        self.fname = self.findChild(QtWidgets.QLineEdit, 'fname_signup')
        self.email = self.findChild(QtWidgets.QLineEdit, 'email_signup')
        self.phone = self.findChild(QtWidgets.QLineEdit, 'phone_signup')
        self.gender = self.findChild(QtWidgets.QComboBox, 'gender_signup')
        self.address = self.findChild(QtWidgets.QLineEdit, 'address_signup')
        self.state = self.findChild(QtWidgets.QComboBox, 'state_signup')
        self.username = self.findChild(QtWidgets.QLineEdit, 'username_signup')
        self.password = self.findChild(QtWidgets.QLineEdit, 'password_signup')

        self.python = self.findChild(QtWidgets.QCheckBox, 'python_signup')
        self.java = self.findChild(QtWidgets.QCheckBox, 'java_signup')
        self.web_design = self.findChild(QtWidgets.QCheckBox, 'web_design_signup')
        self.php = self.findChild(QtWidgets.QCheckBox, 'php_signup')

        self.back = self.findChild(QtWidgets.QPushButton, 'back_signup')
        self.back.clicked.connect(self.go_back)

        self.register_button = self.findChild(QtWidgets.QPushButton, 'signup')
        self.register_button.clicked.connect(self.do_register)
        self.show()

    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()

    def do_register(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            if self.lname.text() == "":
                msgBox.setText("Please Fill In Your Last Name!")
                msgBox.exec_()
            elif self.fname.text() == "":
                msgBox.setText("Please Fill In Your First Name!")
                msgBox.exec_()
            elif self.email.text() == "":
                msgBox.setText("Please Fill In Your Email!")
                msgBox.exec_()
            elif self.phone.text() == "":
                msgBox.setText("Please Fill In Your Phone Number!")
                msgBox.exec_()
            elif self.gender.currentText() == "-Select Gender-":
                msgBox.setText("Please Select Your Gender!")
                msgBox.exec_()
            elif self.address.text() == "":
                msgBox.setText("Please Fill In Your Address!")
                msgBox.exec_()
            elif self.state.currentText() == "-Select State-":
                msgBox.setText("Please Select a State!")
                msgBox.exec_()
            elif self.username.text() == "":
                msgBox.setText("Please Enter A Unique Username!")
                msgBox.exec_()
            elif self.password.text() == "":
                msgBox.setText("Please Enter A Unique Password!")
                msgBox.exec_()
            else:
                Courses = []
                if self.python.isChecked():
                    Courses.append("Python")
                if self.java.isChecked():
                    Courses.append("Java")
                if self.web_design.isChecked():
                    Courses.append("Web_Design")
                if self.php.isChecked():
                    Courses.append("PHP")
                Window.close()
                mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="",
                        database="staff_mgt_system")
                mycusor = mydb.cursor()
                sql = "Insert Into Staff(First_Name, Last_Name, Email, Phone_Number, Gender, Address, State, Course,  Username, Password) " \
                      "Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                Values = (self.fname.text(), self.lname.text(), self.email.text(), self.phone.text(), self.gender.currentText(), self.address.text(),
                          self.state.currentText(), str(Courses), self.username.text(), self.password.text())
                mycusor.execute(sql, Values)
                mydb.commit()
                msgBox.setText("Record Inserted Successfully!!")
                msgBox.exec_()
        except Exception as error:
            print('An Error Occurred', error)

class Setting(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Setting, self).__init__(parent)
        uic.loadUi('settings.ui', self)

        self.emp_id = self.findChild(QtWidgets.QLineEdit, 'emp_id_set')
        self.lname = self.findChild(QtWidgets.QLineEdit, 'lname_set')
        self.fname = self.findChild(QtWidgets.QLineEdit, 'fname_set')
        self.email = self.findChild(QtWidgets.QLineEdit, 'email_set')
        self.phone_number = self.findChild(QtWidgets.QLineEdit, 'phone_number_set')
        self.gender = self.findChild(QtWidgets.QComboBox, 'gender_set')
        self.address = self.findChild(QtWidgets.QLineEdit, 'address_set')
        self.state = self.findChild(QtWidgets.QComboBox, 'state_set')
        self.course = self.findChild(QtWidgets.QLineEdit, 'course_set')
        self.username = self.findChild(QtWidgets.QLineEdit, 'username_set')
        self.password = self.findChild(QtWidgets.QLineEdit, 'password_set')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.back = self.findChild(QtWidgets.QPushButton, 'back_set')
        self.back.clicked.connect(self.go_back)

        self.update_button = self.findChild(QtWidgets.QPushButton, 'update')
        self.update_button.clicked.connect(self.do_update)
        self.show()
        self.front = self.findChild(QtWidgets.QPushButton, 'leaves_set')
        self.front.clicked.connect(self.go_leaves)
        self.front = self.findChild(QtWidgets.QPushButton, 'profile_set')
        self.front.clicked.connect(self.go_profile)
        self.time_table = self.findChild(QtWidgets.QPushButton, 'schedule_set')
        self.time_table.clicked.connect(self.go_time_table)

    def go_time_table(self):
        self.hide()
        menu = Schedule(self)
        menu.show()

    def go_leaves(self):
        self.hide()
        menu = Leave(self)
        menu.show()

    def go_profile(self):
        self.hide()
        menu = Profile(self)
        menu.show()

    def go_back(self):
        self.hide()
        menu = Staff(self)
        menu.show()

    def do_update(self):
        try:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="staff_mgt_system")
            mycusor = mydb.cursor()
            sql = "Update Staff SET First_Name=%s, Last_Name=%s, email=%s, Phone_Number=%s, Gender=%s, Address=%s, State=%s, Course=%s, Username=%s, Password=%s " \
                  "WHERE emp_id=%s"
            Values = (self.fname.text(), self.lname.text(), self.email.text(), self.phone_number.text(), self.gender.currentText(), self.address.text(),
                          self.state.currentText(), self.course.text(), self.username.text(), self.password.text(), self.emp_id.text())
            mycusor.execute(sql, Values)
            mydb.commit()
            msgBox.setText("Record Updated Successfully!!")
            msgBox.exec_()
        except Exception as error:
            print('An Error Occurred', error)

app = QtWidgets.QApplication(sys.argv)
Window = Staff()
app.exec_()
