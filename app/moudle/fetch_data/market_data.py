#   获取行情数据


import akshare as ak
import pandas as pd

# 获取指定日期的涨停股票数据
def get_limitup_stocks(target_date):

    # 获取指定日期的涨停股票数据
    stock_data = ak.stock_zt_pool_em(date=target_date)

    # 如果数据为空，提示用户
    if stock_data.empty:
        print(f"指定日期 {target_date} 没有涨停数据，请确认日期是否为交易日。")
    else:
        # 打印原始数据列名
        print("原始数据列名：", stock_data.columns)
        print("原始数据前几行：", stock_data.head())
        
        # 提取所需的列
        columns_to_keep = ["序号", "代码", "名称", "涨跌幅", "最新价" ,"总市值", "换手率", "炸板次数", "涨停统计","连板数", "所属行业"]
        filtered_data = stock_data[columns_to_keep].copy()

        # 检查并处理数据类型
        filtered_data["涨跌幅"] = pd.to_numeric(
            filtered_data["涨跌幅"].astype(str).str.rstrip('%'), errors="coerce"
        )
        filtered_data["最新价"] = pd.to_numeric(filtered_data["最新价"], errors="coerce")

        # # 筛选条件
        filtered_data = filtered_data[

            (filtered_data["最新价"] < 5)
            &(filtered_data["总市值"]/100000000<100)
            &(filtered_data["涨跌幅"] < 11)
        ]

        # 保存为 Excel 文件
        output_filename = f"{target_date}当天涨停市值小于100亿.xlsx"
        filtered_data.to_excel(output_filename, index=False)

        print(f"筛选后的数据已保存为 {output_filename}")