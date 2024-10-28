

from PySide6.QtCore import *
from Controller.sepController import Sep
import time
from utils import *

class ThreadSep(QThread):

    signal_update = Signal(object, object)

    def __init__(self, index_thread, id_profile, type_browser, api_key, selected_version):
        super(ThreadSep, self).__init__()
        self.index_thread = index_thread
        self.id_profile = id_profile
        self.type_browser = type_browser
        self.api_key = api_key
        self.selected_version = selected_version

    def run(self):
        self.signal_update.emit(self.index_thread, [self.index_thread, "xxxx", "Đang khởi tạo trình duyệt..."])
        self.auto = Sep(
            type_browser=self.type_browser,
            position=self.index_thread, 
            api_key=self.api_key,
            path_folder_profile=r"C:\Users\Admin\AppData\Local\Google\Chrome\User Data",
            id_profile=self.id_profile,
            selected_version=self.selected_version
        )

        success = 0
        while True:
            self.signal_update.emit(self.index_thread, [self.index_thread, "xxxx", f"Đang tạo acc lần thứ {success}..."])
            self.auto.register()
            # write_txt_a(path=r"C:\Users\Admin\Desktop\code tool\Buổi 567\accs\accs.txt", data=[mail])
            self.auto.logout()
            success += 1

    def stop(self):
        self.signal_update.emit(self.index_thread, [self.index_thread, "xxxx", "Đã dừng!"])
        try:
            self.auto.driver.close()
            self.auto.driver.quit()
        except:
            pass
        self.terminate()


