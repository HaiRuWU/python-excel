# hairu, wu
# 2021/7/11

# 读取表格文件，统计青年大学习次数

# 下载表格文件
import os
import urllib.request


def get_file():
    foler_name = "./files"
    if not os.path.exists(foler_name):
        os.makedirs(foler_name)
    # urls
    list = {}
    list['week3'] = 'hw.xlsx'
    list['week4'] = 'h.xlsx'
     # 遍历下载文件
    for key in list:
        try:
            file_name = foler_name + '/' + key + ".xlsx"
            urllib.request.urlretrieve(list[key], filename=file_name)
            print(file_name + "success!")
        except Exception as e:
            print(file_name + "error!")

if __name__ == '__main__':
    get_file()

