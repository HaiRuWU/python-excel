
# 分析files表格文件数据，获取青年大学习信息
import os
import pandas as pd

if __name__ == '__main__':
    print("开始统计青年大学习结果！")
    result = {}
    week = []
    # {week_x: [{name1:type1},{name2:type2},...]}
    # 读文件
    foler_name = './files'
    files = os.listdir(foler_name)
    for file_name in files:
        # 保存星期名称
        week.append(file_name[0:file_name.index('.')])
        #
        result[file_name] = []
        # 对于每一个文件名，读取文件
        excel = pd.read_excel(foler_name + '/' + file_name, usecols=[3, 5])
        data = excel.values
        # 对每一个人
        for user in data:
            value = {}
            value[user[0]] = user[1]
            result[file_name].append(value)

    # 对于result中的数据，统计信息
    #     week1 week2 week3...
    # 姓名  yes    yes     no

    # 最终格式为：{name:[week1, week2 , ...]}
    final_result = {}
    for weeK_key in result:
        # week_key 星期几
        # result[week_key] 用户数据
        for user in result[weeK_key]:
            for key in user:
                if key in final_result:
                    final_result[key].append(int(weeK_key[4:weeK_key.index('.')]))
                else:
                    final_result[key] = []
                    final_result[key].append(int(weeK_key[4:weeK_key.index('.')]))


    # 整理成表格形式
    data_frame = {}
    data_frame['demo'] = []
    for wk in week:
        data_frame['demo'].append(wk)

    for name in final_result:
        data_frame[name] = []
        # 遍历所有的week，比较当前的week是否在这个人的已打卡范围内
        for wk_str in week:
            flag = False
            for wk in final_result[name]:
                # 在打卡范围内
                if int(wk_str[4:]) == wk:
                    flag = True
                    break
            if flag:
                data_frame[name].append("yes")
            else:
                data_frame[name].append("  ")
    # 写文件
    result_excel = pd.DataFrame(
        data_frame.values(),
        index=data_frame.keys(),
    )
    file_path = './data/青年大学习统计.xlsx'
    result_excel.to_excel(file_path)
    # writer = pd.ExcelWriter(file_path)
    print("导出青年大学习统计结果成功！")
    pass