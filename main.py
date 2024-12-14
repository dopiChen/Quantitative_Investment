# app/services/data_loader.py
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from app.db.connection import engine
import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528', adjust="")

from sqlalchemy.types import String, Float, Integer, Date

dtype_mapping = {
    "日期": Date,
    "股票代码": String(10),
    "开盘": Float,
    "收盘": Float,
    "最高": Float,
    "最低": Float,
    "成交量": Integer,
    "成交额": Float,
    "振幅": Float,
    "涨跌幅": Float,
    "涨跌额": Float,
    "换手率": Float,
}

stock_zh_a_hist_df.to_sql("history_daily_data", con=engine, if_exists="replace", index=False, dtype=dtype_mapping)