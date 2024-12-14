import pandas as pd
from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from app.db.connection import engine

def load_data_to_database(file_path):
    """
    将 Excel 数据加载到数据库
    """
    # 加载数据
    result_df = pd.read_excel(file_path, dtype={"代码": str})
    #
    # 确保 '代码' 列为 6 位字符串（补齐前导零）
    result_df["代码"] = result_df["代码"].str.zfill(6)

    dtype_mapping = {
    "序号": Integer,
    "代码": String(6),
    "名称": String(50),
    "市盈率-动态":Float,
    "总市值": Float,
    }

    try:
        # 将数据写入数据库
        result_df.to_sql("company_data", con=engine, if_exists="replace", index=False, dtype=dtype_mapping)
        print("数据成功写入数据库")
    except SQLAlchemyError as e:
        print(f"数据写入失败: {e}")



if __name__ == '__main__':
    load_data_to_database("/Users/chenlintao/codes/Quantitative_Investment/data/filtered_stocks_cleaned.xlsx")
    