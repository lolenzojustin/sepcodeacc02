from Controller.sepBrowserController import *
from utils import *
import random
import os
import gspread
# max_retries = 100  # Số lần thử tối đa
# attempt = 0  # Biến đếm số lần thử
credentials = {
    "type": "service_account",
    "project_id": "septoolacc",
    "private_key_id": "f656da81002ac1e920d95576a8a598a43c30452e",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDL90NNjC//FVRb\ns3WdntZNSvdkVab4INGQ8Rt0ge5Z62nLWa+G+dUp9PO75cHSzPOQ7gLtG/S7WnNJ\nVt3eh+yq7TxWpD/J898MIL/vOWwFWy/b1xW5h1a9Mk+HsFIm53QMJPAhypSG44/i\nvSG2XYSwvl+bYPIb7vOmDoU/jpY+5vq7HCj+EuJ6NZ+9VVNadlYWiTXGvMUX3geu\nZYuX/oC9qhFPrT42dnMMK4Ep8WUvfrov3kbk9HsZE/mf2XeVCO0ilsKytIHI6K15\nZziN/DwCOUlC2oq3ZIQRXy5dxh/LyZc4iuMPCkvxJrYNYKL+7zZ2DAzo8mo9USZq\nBBIhIipZAgMBAAECggEACWangXwup3vc3C/UrKPU43x1vqLRWVUZ6QD+mkt1faDY\nys34Gyk0vARVn5l4FOFBcLKntooNU6gC8aRsAYUTps/cchnhSXZQwjGtkbcnKsVd\n2qzP4YdCu4xawg73GmKcpK/8fseO5PtkIbfvRS/g8ncz15OLqoyZn6kXrIBD8zjZ\nJhlId8RmgWOUTq7LVlYHb10Wa13mcKTmOcz5OQpjxY6wu8MQgMEtdjEw03GV58lk\nh+pSirsEincVyn6paJRWVXtxKoShhd5uZuvI1YM48gBMMxkuWUguqhbSVL3gxRYZ\neiqvnMUwv04fCDvnIXh9+eZ6e93oYjajlrsiSCEZyQKBgQDnLC/shvylO0iNn+R3\n1WR+Pxzc95HZ2mGCCovXjlb50FIrbxdPX4Yj3uMrzUv7Kin8tikbIbvXqcUNnxcF\nLraPx3e2hfyWktFZa+Fbt8WaDUOB4JQ+xGHRm73m4bhD45AonxD6Re4VnMhDx+xc\nko0IU8O242IVGV2XBWO6oVPkKwKBgQDh3w8pVfYC5kVZVsBLWY/pzak3J0exkHvi\nII540ypBRHuxsJP9UaBmghb6vTnH64N+tNjXCW5f9iXwG0aqD0b8wb5g0Ic2bS6j\nxbIt3EEL2LfIHPILyGvY+CGcYlQ+FA0IMxXBDk+OCBPIHuYQETmalHyCWD8CIdSr\n7BuYQPlViwJ/b/j3PZokxePxQKgyAdla08u+L0m7W8prcJGrKr3HYzmEk4U7xTZ/\nwuAzKQRHyWCi9cVGI94zHkMdL3vfqqL1yq7TTZWYw1ZaEPYwMjzReczy5fXh2IVG\n3ECTu0GZ/0g6i3KAxrkYmV9XoX00/6H8rgvkwLFi0NV4f64coEmEWQKBgQDKtuji\njlWmsIfY8HTQq2bvzTZrW4OKp0On5NQ5ODuaLB5fkTygg1vT5Dk/fAiZlpODakea\nZsp6sW3HGpPHGML7Id79AOn5PPA457tMUXrHaQ84OFI7pPq11axEsDMvK8uuajrB\n81gO/szSNHkCPpNWWqGMUirqfPZj/hmeAeJElQKBgQDmGBbkuGrl7AFJNGbSK+ha\nQoAPM6SNmVZLhORF8UlNlqud7rpdXobOIjmROeTuouU89cfL1Xqelid96sOI3xkE\n0pEvXVAOdn7olC6hdNQAg3PBh+QPi3vJFkeKv1BgeO9qep/N0RyUlmdvKXWMi/Qy\n8MSDM7+6fzvDb4pqL+NR3A==\n-----END PRIVATE KEY-----\n",
    "client_email": "septoolacc@septoolacc.iam.gserviceaccount.com",
    "client_id": "107253161766531622071",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/septoolacc%40septoolacc.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
class Sep(SepBrowser):
    def __init__(self, type_browser, position, api_key, path_folder_profile, id_profile,selected_version) -> None:
        super().__init__(type_browser = type_browser, position=position, api_key=api_key, path_folder_profile=path_folder_profile, id_profile=id_profile,selected_version=selected_version)

        # self.do_click(by_located=(By.XPATH,"//button[@data-at='hihi']"), timeout=99999)
        self.thang = []
        self.thang_1 = ['thang1','j']
        self.thang_2 = ['thang2', 'f']
        self.thang_3 = ['thang3','m']
        self.thang_4 = ['thang4','a']
        self.thang_5 = ['thang5','mm']
        self.thang_6 = ['thang6','jj']
        self.thang_7 = ['thang7','jjj']
        self.thang_8 = ['thang8','aaa']
        self.thang_9 = ['thang9','s']
        self.thang_10 = ['thang10','o']
        self.thang_11 = ['thang11','n']
        self.thang_12 = ['thang12','d']
        if selected_version == "tháng 1":
            self.thang = self.thang_1
        elif selected_version == "tháng 2":
            self.thang = self.thang_2
        elif selected_version == "tháng 3":
            self.thang = self.thang_3
        elif selected_version == "tháng 4":
            self.thang = self.thang_4
        elif selected_version == "tháng 5":
            self.thang = self.thang_5
        elif selected_version == "tháng 6":
            self.thang = self.thang_6
        elif selected_version == "tháng 7":
            self.thang = self.thang_7
        elif selected_version == "tháng 8":
            self.thang = self.thang_8
        elif selected_version == "tháng 9":
            self.thang = self.thang_9
        elif selected_version == "tháng 10":
            self.thang = self.thang_10
        elif selected_version == "tháng 11":
            self.thang = self.thang_11
        elif selected_version == "tháng 12":
            self.thang = self.thang_12

        # In ra danh sách self.thang để kiểm tra
        print("Danh sách thang hiện tại:", self.thang)
    def append_row (self,ggsheet_name, tab_name, row_value):
        gs = gspread.service_account_from_dict(credentials)
        sheet = gs.open(ggsheet_name)
        worksheet = sheet.worksheet(tab_name)
        worksheet.append_row(row_value, table_range="A1:B1")
    
    def register(self):

        list_number = ['1','2','3','4','5','6','7','8','9','0']
        random_phone = (random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number))
        list_day = ['1','2','3','4','5', '6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29']
        random_day = (random.choice(list_day))
        random_email = (
            random.choice(list_number)
            + random.choice(list_number)
            + random.choice(list_number)
            + random.choice(list_number)
            + self.thang[0]
            + "atsep@lolenzo.top"
        )
        # self.driver.get("https://www.sephora.com/ca/en/")
        # time.sleep(2000)
        self.driver.get("https://www.sephora.com/profile/MyAccount/Orders")

        self.driver.refresh()
        time.sleep(2)
        # self.do_click(by_located=(By.XPATH,"//button[@data-comp='Icon StyledComponent']"), timeout=100)
        # self.do_click(by_located= (By.XPATH,"//button[@type = 'button']"), timeout= 100 )
        while self.do_click(by_located=(By.XPATH,"//button[@data-at='create_account_button']"), timeout=3) == False:
            time.sleep(3)
            print("bấm tạo tk")
        # time.sleep(1)
        # self.do_sendkeys(by_located=(By.XPATH,"//input[@autocomplete = 'email']"), timeout=100, text="sdasdasdsa@lolenzo.top")
        while self.do_sendkeys_slow(by_located=(By.ID, "email"), timeout=1000, text=random_email) == False:
            time.sleep(3)
        print("đã send mail ", random_email)
        # self.do_sendkeys_slow(by_located=(By.CLASS_NAME, "css-290f3n"), timeout=100, text=random_email)
        # self.do_sendkeys_slow(by_located=(By.ID, "email"), timeout=100, text=random_email)
        # sleep_very_short()
        # if self.check_text(text="Continue", timeout=100):
        #     self.do_click(by_located=(By.XPATH,"//button[@type = 'submit']"), timeout= 10 )
        #     self.do_click(by_located=(By.XPATH,"//button[@class = 'css-1eg024x eanm77i0']"), timeout= 100 )
        while self.do_click(by_located=(By.XPATH,"//button[@type = 'submit' and text()='Continue']"), timeout= 3 ) == False:
            time.sleep(3)
        # sleep_short()
        # self.do_click(by_located=(By.XPATH,"//button[@class = 'css-1eg024x eanm77i0']"), timeout= 100 )
        # if self.check_text(text="Create An Account", timeout=100):
        if self.check_element_exists(by_located=(By.ID, "firstName"), timeout=3):  
            print ("đã check đc element first name")
        while self.do_sendkeys_slow(by_located=(By.ID, "firstName"), timeout=10, text="sep") == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "lastName"), timeout=10, text=random_day) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "register_password"), timeout=10, text="Thang@123") == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "mobilePhone"), timeout=10, text=random_phone) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "zipCode"), timeout=10, text="V8W 2J8") == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegMonth']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "biRegMonth"), timeout=10, text=self.thang[1]) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegMonth']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegDay']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "biRegDay"), timeout=10, text=random_day) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegDay']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        # self.do_click(by_located=(By.XPATH,"//select[@class='css-lbyitw Checkbox-box']"), timeout=3)
        while self.do_click(by_located=(By.XPATH,"//button[@data-at='join_now']"), timeout=3) == False:
            time.sleep(3)
        print("add vào sheet")

        self.append_row(ggsheet_name="DataSep", tab_name="Tab1", row_value=[random_email])
        # if self.check_text(text="Looks like you are trying to access", timeout=6):
        # if self.check_element_exists(by_located=(By.XPATH, "//button[@data-at='modal_body']"), timeout=6):
        if self.check_text(text="Looks like you are trying to access", timeout=6):
            print("đã tìm thấy ")
            while self.do_click(by_located=(By.XPATH, "//button[@data-at='modal_close']"), timeout=2) == False:
                time.sleep(2)
                print("time = 6 ")
    def logout(self):

        while self.do_click(by_located=(By.XPATH,"//button[@data-at='account_btn']"), timeout=3) == False:
            time.sleep(2)
            print("Thử logout tiếp ...")
        time.sleep(1)
        while self.do_click_js(by_located=(By.XPATH,"//button[@data-at='sign_out_button']"), timeout=3) == False:
            time.sleep(2)
            print("bấm logout")
        time.sleep(3)

       

