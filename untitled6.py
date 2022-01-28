import matplotlib.pyplot as plt
import speedtest
import time

list_upload = []
list_download = []

for i in range(5):
    st = speedtest.Speedtest()
    download_speed = round(st.download()/10000000,2)
    list_download.append(download_speed)
    upload_speed = round(st.upload()/10000000,2)
    list_upload.append(upload_speed)
    
    time.sleep(60)
    print(list_download)
    print(list_upload)
    
x = [1,2,3,4,5,]
    
plt.plot(x,list_download, label = "Download Speed")
plt.title('Speed')
plt.plot(x,list_upload, label = "Upload Speed")
plt.legend()
plt.show()
