#   获取个股数据

import akshare as ak
import pandas as pd


def get_stockdata_toexcel(start_date, end_date,symbol):
    # 获取中国银行symbol股票的历史日线数据
    try:
        stock_data = ak.stock_zh_a_hist(symbol=symbol, start_date=start_date, end_date=end_date,adjust='')
        if stock_data is None or stock_data.empty:
            print("没有获取到数据，可能是网络问题或者股票代码格式不正确。")
        else:
            # 提取需要的列
            stock_filtered = stock_data[["日期", "开盘", "收盘", "涨跌幅"]]

            # 保存为 Excel 文件
            file_name = symbol+".xlsx"
            stock_filtered.to_excel(file_name, index=False, engine='openpyxl')

            print(f"数据已保存为 {file_name}")
    except Exception as e:
        print(f"发生错误: {e}")


def fetch_history_daily_data(symbol, start_date, end_date):
    stock_data = ak.stock_zh_a_hist(symbol=symbol, start_date=start_date, end_date=end_date, adjust='')
    return stock_data

