import requests
from bs4 import BeautifulSoup as bs  # bs4 库 BeautifulSoup为包
import pandas as pd

# 前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
url = 'https://maoyan.com/films?showType=3'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
cookie = 'BIDUPSID=C4165988E0B9E5C5748C49AEDD965525; PSTM=1591239422; BAIDUID=C4165988E0B9E5C53D7F3D15FA58A53F:FG=1; HMACCOUNT=6AB95F4BD4173384; BDUSS=UE4VDZGUHBWYnVjMG9KQ0FUMGJoWHo4aGVrODh6WDdDamFZQk5PMjF4UWRNUWRmRVFBQUFBJCQAAAAAAAAAAAEAAABJdCNU1ea1xLrcxNHIpbCuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2k314dpN9eU; cflag=13%3A3; HMVT=24f17767262929947cc3631f99bfd274|1593408378|6bcd52f51e9b3dce32bec4a3997715ac|1593409765|'
header = {'user-agent': user_agent, 'Cookie': cookie}

# 无header的话就会被拦截，无法正常获取网页
response = requests.get(url, headers=header)
# 打印浏览器的返回码
print(f'返回码是：{response.status_code}')
bs_info = bs(response.text, 'html.parser')

data = pd.DataFrame()
for tag in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    if len(data) > 9:
        break
    # 获取电影名称
    name = tag.find('span', attrs={'class': 'name'}).text
    type = ""
    date = ""

    for info in tag.find_all('div', attrs={'class': 'movie-hover-title'}):
        # print(info.text.strip()[0:2])
        if info.text.strip()[0:2] == '类型':
            #    print(info.text.strip())  # 获取电影类型
            type = info.text.strip()
        if info.text.strip()[0:2] == "上映":
            #    print(info.text.strip())  # 获取电影上映时间
            date = info.text.strip()

    mylist={'电影名称':name,'电影类型':type,'上映日期':date}
  #  print(mylist)
    data=data.append(mylist,ignore_index=True)

data.to_csv("maoyanmovie.csv",encoding="utf_8_sig")