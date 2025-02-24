import codecs

import pandas as pd
import sys

def analyze_data_and_generate_query(csv_file_path):

    sys.stdout = sys.stdout.detach()
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    # 读取CSV文件
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        return f"Error reading CSV file: {e}"

    # 检查需要的列是否存在
    required_columns = ['RRU.PrbUsedDl', 'RRU.PrbUsedUl', 'DRB.UEThpDl', 'DRB.UEThpUl']
    for column in required_columns:
        if column not in df.columns:
            return f"Missing required column: {column}"

    # 提取需要的特征值
    prb_used_dl = df['RRU.PrbUsedDl'].iloc[0:20].tolist()  # 取前20行数据作为示例
    prb_used_ul = df['RRU.PrbUsedUl'].iloc[0:20].tolist()  # 取前20行数据作为示例
    ue_thp_dl = df['DRB.UEThpDl'].iloc[0:20].tolist()  # 取前20行数据作为示例
    ue_thp_ul = df['DRB.UEThpUl'].iloc[0:20].tolist()  # 取前20行数据作为示例

    # 生成分析文本
    query = f"""
    网络优化建议：

    1. 下行吞吐量分析:
    - DRB.UEThpDl（下行吞吐量）为: {ue_thp_dl}，表示用户占用的业务量，取决于用户请求和资源分配情况。
    - RRU.PrbUsedDl（下行资源使用量）为: {prb_used_dl}，是网络自有资源的使用量。

    2. 上行吞吐量分析:
    - DRB.UEThpUl（上行吞吐量）为: {ue_thp_ul}，表示上行的用户占用资源情况。
    - RRU.PrbUsedUl（上行资源使用量）为: {prb_used_ul}，是网络自有资源的上行使用量。

    请根据以上数据进行网络优化建议。
    """

    return query

if __name__ == '__main__':
    # 检查是否提供了文件路径作为命令行参数
    if len(sys.argv) != 2:
        print("Usage: python huoshan_deepseek.py <csv_file_path>")
        sys.exit(1)

    # 获取CSV文件路径
    csv_file_path = sys.argv[1]

    # 生成查询文本
    query = analyze_data_and_generate_query(csv_file_path)

    # 输出生成的查询文本
    print(query)
