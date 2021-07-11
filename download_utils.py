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
    list['week3'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180703/41d0cfc/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week4'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180715/c28db12/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week5'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180726/1bbdf4d/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week6'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180739/7bc0ef5/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week7'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180748/e20ae0f/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week8'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180759/dbe50ea/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week9'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180812/902e3eb/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week11'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180822/3f7ed74/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week13'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180833/9f55042/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week14'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180844/a2e5fd7/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week15'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180854/bf02ac5/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week16'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180903/8ee01c3/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week17'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180913/d7621f4/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
    list['week18'] = 'https://7072-production-qzrww-1300967099.tcb.qcloud.la/excel/2021-07-10/2021-07-10-180922/b15d06f/%E7%BE%A4%E6%94%B6%E9%9B%86%E5%B0%8F%E7%A8%8B%E5%BA%8F.xlsx'
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

