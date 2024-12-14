# 添加个股历史数据
import pandas as pd
from sqlalchemy import Date, Float, Integer, String
from app.moudle.fetch_data.individual_stock_data import fetch_history_daily_data
from app.db.connection import engine

def load_history_data_to_database( file_path,start_date, end_date,start_index, end_index):
    # file_path : 公司股票代码列表文件路径
    # start_date : 开始日期
    # end_date : 结束日期
    # start_index : 起始索引
    # end_index : 结束索引

    #读取公司股票代码列表
    company_list = pd.read_excel(file_path,dtype={"代码": str})
    # 限制当前批次的公司范围
    company_batch = company_list.iloc[start_index:end_index]
    # 定义数据库映射表
    dtype_mapping = {
    "日期": Date,                 # 日期类型
    "股票代码": String(6),         # 股票代码，固定长度6
    "开盘": Float,                # 开盘价
    "收盘": Float,                # 收盘价
    "最高": Float,                # 最高价
    "最低": Float,                # 最低价
    "成交量": Integer,            # 成交量，整数
    "成交额": Float,              # 成交额
    "振幅": Float,                # 振幅
    "涨跌幅": Float,              # 涨跌幅
    "涨跌额": Float,              # 涨跌额
    "换手率": Float               # 换手率
    }

    # 遍历公司列表，获取每个公司的历史数据
    for code in company_batch["代码"]:
        # 获取历史数据
        df = fetch_history_daily_data(code,start_date, end_date)
        # 将数据写入数据库
        df.to_sql("history_daily_data", engine, if_exists="append", index=False, dtype=dtype_mapping)
        # 打印成功信息
        print(f"成功写入{code}的历史数据")
    print("所有指定公司历史数据写入完成")


if __name__ == "__main__":
    file_path = "/Users/chenlintao/codes/Quantitative_Investment/data/filtered_stocks_cleaned.xlsx"
    load_history_data_to_database(file_path,"20230101","20241201",2001,3076)

        




