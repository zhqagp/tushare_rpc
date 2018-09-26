#!/usr/local/bin/python3.7

from flask import Flask, request

import json

import tushare as ts


app = Flask(__name__)

ts.set_token('177ab952b023be1c941dcf9e8c852c3bb0727502a2f372fa731d607e')
pro = ts.pro_api()

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/pro/stock_basic", methods=['POST'])
def pro_stock_basic():

    df = pro.stock_basic(exchange_id=request.form['exchange_id'], is_hs=request.form['is_hs'], fields='ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_date,list_status,delist_date,is_hs')

    return df.to_json(orient='table')


@app.route("/pro/trade_cal", methods=['POST'])
def pro_trade_cal():

    df = pro.trade_cal(exchange_id=request.form['exchange_id'], start_date=request.form['start_date'], end_date=request.form['end_date'])

    return df.to_json(orient='table')


@app.route("/pro/namechange", methods=['POST'])
def pro_namechange():

    df = pro.namechange(ts_code=request.form['ts_code'], fields='ts_code,name,start_date,end_date,change_reason')

    return df.to_json(orient='table')

@app.route("/pro/hs_const", methods=['POST'])
def pro_hs_const():

    df = pro.hs_const(hs_type=request.form['hs_type'])

    return df.to_json(orient='table')


@app.route("/pro/daily", methods=['POST'])
def pro_daily():

    df = pro.daily(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')



@app.route("/pro/adj_factor", methods=['POST'])
def pro_adj_factor():

    df = pro.adj_factor(ts_code=request.form['ts_code'],trade_date=request.form['trade_date'])

    return df.to_json(orient='table')


@app.route("/pro/suspend", methods=['POST'])
def pro_suspend():

    df = pro.suspend(ts_code=request.form['ts_code'],suspend_date=request.form['suspend_date'],resume_date=request.form['resume_date'],fiedls='')

    return df.to_json(orient='table')



@app.route("/pro/daily_basic", methods=['POST'])
def pro_daily_basic():

    df = pro.daily_basic(ts_code=request.form['ts_code'],trade_date=request.form['trade_date'])

    return df.to_json(orient='table')


@app.route("/pro/income", methods=['POST'])
def pro_income():

    df = pro.income(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')


@app.route("/pro/balancesheet", methods=['POST'])
def pro_balancesheet():

    df = pro.balancesheet(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')


@app.route("/pro/cashflow", methods=['POST'])
def pro_cashflow():

    df = pro.cashflow(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')


@app.route("/pro/dividend", methods=['POST'])
def pro_dividend():

    df = pro.dividend(ts_code=request.form['ts_code'])

    return df.to_json(orient='table')


@app.route("/pro/express", methods=['POST'])
def pro_express():

    df = pro.express(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')


@app.route("/pro/fina_indicator", methods=['POST'])
def pro_fina_indicator():

    df = pro.fina_indicator(ts_code=request.form['ts_code'])

    return df.to_json(orient='table')


@app.route("/pro/fina_audit", methods=['POST'])
def pro_fina_audit():

    df = pro.fina_audit(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')


@app.route("/pro/fina_mainbz", methods=['POST'])
def pro_fina_mainbz():

    df = pro.fina_mainbz(ts_code=request.form['ts_code'],period=request.form['period'],type=request.form['type'])

    return df.to_json(orient='table')


@app.route("/pro/moneyflow_hsgt", methods=['POST'])
def pro_moneyflow_hsgt():

    df = pro.moneyflow_hsgt(start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')

@app.route("/pro/hsgt_top10", methods=['POST'])
def pro_hsgt_top10():

    df = pro.hsgt_top10(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'],trade_date=request.form['trade_date'],market_type=request.form['market_type'])

    return df.to_json(orient='table')



@app.route("/pro/ggt_top10", methods=['POST'])
def pro_ggt_top10():

    df = pro.ggt_top10(trade_date=request.form['trade_date'])

    return df.to_json(orient='table')



@app.route("/pro/margin", methods=['POST'])
def pro_margin():

    df = pro.margin(trade_date=request.form['trade_date'])

    return df.to_json(orient='table')



@app.route("/pro/margin_detail", methods=['POST'])
def pro_margin_detail():

    df = pro.margin_detail(trade_date=request.form['trade_date'],ts_code=request.form['ts_code'])

    return df.to_json(orient='table')


@app.route("/pro/top10_holders", methods=['POST'])
def pro_top10_holders():

    df = pro.top10_holders(ts_code=request.form['ts_code'],start_date=request.form['start_date'],end_date=request.form['end_date'])

    return df.to_json(orient='table')



@app.route("/pro/top10_floatholders", methods=['POST'])
def pro_top10_floatholders():

    df = pro.top10_floatholders(start_date=request.form['start_date'],end_date=request.form['end_date'],ts_code=request.form['ts_code'])

    return df.to_json(orient='table')


@app.route("/pro/index_basic", methods=['POST'])
def pro_index_basic():

    df = pro.index_basic(market=request.form['market'])

    return df.to_json(orient='table')


@app.route("/pro/index_daily", methods=['POST'])
def pro_index_daily():

    df = pro.index_daily(ts_code=request.form['ts_code'])

    return df.to_json(orient='table')


@app.route("/pro/index_weight", methods=['POST'])
def pro_index_weight():

    df = pro.index_weight(index_code=request.form['index_code'],trade_date=request.form['trade_date'])

    return df.to_json(orient='table')

@app.route("/pro/tmt_twincome", methods=['POST'])
def pro_tmt_twincome():

    df = pro.tmt_twincome(item=request.form['item'])

    return df.to_json(orient='table')


@app.route("/pro/tmt_twincomedetail", methods=['POST'])
def pro_tmt_twincomedetail():

    df = pro.tmt_twincomedetail(item=request.form['item'],symbol=request.form['symbol'])

    return df.to_json(orient='table')


if __name__ == "__main__":
    app.run(debug=True)
