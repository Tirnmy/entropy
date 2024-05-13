"""
将一天分为24个时间段，每个时间段长度为1小时，计算饮食活动的时间熵
"""

import matplotlib.pyplot as plt
import pandas as pd


def get_plot(df_diet, id):
    """
    获取某学生的饮食活动次数时间折线图
    :param df_diet:
    :param id:
    :return:
    """
    df_diet = df_diet.loc[df_diet['id'] == id, :]
    df_plot = pd.DataFrame()
    df_plot[['timestamp', 'behavior']] = df_diet.loc[:, ['time', 'action']]

    # 将时间转换为datetime对象
    df_plot['timestamp'] = pd.to_datetime(df_plot['timestamp']).dt.time

    # 提取小时信息，将每个时间点分类到对应的小时时间段
    df_plot['hour_bin'] = df_plot['timestamp'].apply(lambda x: x.hour)

    # 统计每个小时内学生的行为次数
    behavior_counts = df_plot.groupby(['hour_bin', 'behavior']).size().unstack(fill_value=0)

    # 绘制折线图
    plt.rcParams['font.family'] = 'SimHei'
    plt.figure(figsize=(12, 8))

    # 对每个行为绘制一条线
    for behavior in behavior_counts.columns:
        plt.plot(behavior_counts.index, behavior_counts[behavior], marker='o', label=behavior)

    # 设置x轴和y轴的标签
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Behaviors')
    plt.title(id + ':' + 'Line Chart of Student Behaviors by Hour')

    # 添加图例
    plt.legend()
    plt.savefig('../data/data-05-08/img/activity-number/' + id + '.png')
    plt.show()


if __name__ == '__main__':
    f_path = '../data/allstudent.csv'
    df = pd.read_csv(f_path)
    df_diet = df.loc[df['action'].isin(['吃早饭', '吃中饭', '吃晚饭']), :].astype('str')
    stu_lst = ['201610329', '201610219', '201610210', '201740134', '201610103']

    # # 获取饮食活动次数折线图
    # for id in stu_lst:
    #     get_plot(df_diet, id)

