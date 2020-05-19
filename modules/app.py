from modules.odd_even import OddEven
from models.file_handling import FileHandling
from modules.send_email import SendEmail

if __name__ == '__main__':
    obj = SendEmail()
    obj_1 = OddEven()
    obj_2 = FileHandling()
    obj_2.addition()

