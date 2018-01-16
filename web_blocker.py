import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = r"/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com"]

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now()
    < dt(dt.now().year, dt.now().month, dt.now().day, 18)):
        print("working hours")
        with open(hosts_path,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                #'any' takes a list as input, to iterate
                    file.write(line)
            file.truncate()
            #truncate , to cut off. It means cutting off all the text after this point
        print("not in the time zone")
    time.sleep(30)
