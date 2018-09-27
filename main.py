#!/usr/local/bin/python3.7

from flask import Flask, request

import json

import tushare as ts


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


#历史行情
# code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
# start：开始日期，格式YYYY-MM-DD
# end：结束日期，格式YYYY-MM-DD
# ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0

@app.route("/get_hist_data", methods=['POST'])
def get_hist_data():

    df = ts.get_hist_data(code=request.form['code'], start=request.form['start'], end=request.form['end'],ktype=request.form['ktype'])

    return df.to_json(orient='table')

@app.route("/get_stock_basics", methods=['POST'])
def get_stock_basics():

    df = ts.get_stock_basics(code=request.form['code'], start=request.form['start'], end=request.form['end'],ktype=request.form['ktype'])

    return df.to_json(orient='table')


# 复权数据
# code:string,股票代码 e.g. 600848
# start:string,开始日期 format：YYYY-MM-DD 为空时取当前日期
# end:string,结束日期 format：YYYY-MM-DD 为空时取去年今日
# autype:string,复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
# index:Boolean，是否是大盘指数，默认为False
# retry_count : int, 默认3,如遇网络等问题重复执行的次数
# pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

@app.route("/get_h_data", methods=['POST'])
def get_h_data():

    df = ts.get_h_data(code=request.form['code'], start=request.form['start'], end=request.form['end'],autype=request.form['autype'],index=request.form['index'])

    return df.to_json(orient='table')


@app.route("/get_today_all", methods=['POST'])
def get_today_all():

    df = ts.get_today_all()

    return df.to_json(orient='table')


@app.route("/get_realtime_quotes", methods=['POST'])
def get_realtime_quotes():

    df = ts.get_realtime_quotes(symbols=request.form['symbols'])

    return df.to_json(orient='table')


@app.route("/get_today_ticks", methods=['POST'])
def get_today_ticks():

    df = ts.get_today_ticks(code=request.form['code'])

    return df.to_json(orient='table')


@app.route("/get_index", methods=['POST'])
def get_index():

    df = ts.get_index()

    return df.to_json(orient='table')


@app.route("/get_sina_dd", methods=['POST'])
def get_sina_dd():

    df = ts.get_sina_dd(code=request.form['code'], date=request.form['date'])

    return df.to_json(orient='table')




@app.route("/profit_data", methods=['POST'])
def profit_data():

    df = ts.profit_data(year=request.form['year'],top=int(request.form['top']))

    return df.to_json(orient='table')


@app.route("/forecast_data", methods=['POST'])
def forecast_data():

    df = ts.forecast_data(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')



@app.route("/xsg_data", methods=['POST'])
def xsg_data():

    df = ts.xsg_data(year=int(request.form['year']),month=int(request.form['month']))

    return df.to_json(orient='table')



@app.route("/fund_holdings", methods=['POST'])
def fund_holdings():

    df = ts.fund_holdings(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')



@app.route("/new_stocks", methods=['POST'])
def new_stocks():

    df = ts.new_stocks()

    return df.to_json(orient='table')


@app.route("/sh_margins", methods=['POST'])
def sh_margins():

    df = ts.sh_margins(start=request.form['start'], end=request.form['end'])

    return df.to_json(orient='table')


@app.route("/sh_margin_details", methods=['POST'])
def sh_margin_details():

    df = ts.sh_margin_details(date=request.form['date'],symbol=request.form['symbol'],start=request.form['start'], end=request.form['end'])

    return df.to_json(orient='table')


@app.route("/sz_margins", methods=['POST'])
def sz_margins():

    df = ts.sz_margins(start=request.form['start'], end=request.form['end'])

    return df.to_json(orient='table')


@app.route("/sz_margin_details", methods=['POST'])
def sz_margin_details():

    df = ts.sz_margin_details(date=request.form['date'])

    return df.to_json(orient='table')



@app.route("/get_industry_classified", methods=['POST'])
def get_industry_classified():

    df = ts.get_industry_classified()

    return df.to_json(orient='table')


@app.route("/get_concept_classified", methods=['POST'])
def get_concept_classified():

    df = ts.get_concept_classified()

    return df.to_json(orient='table')




@app.route("/get_area_classified", methods=['POST'])
def get_area_classified():

    df = ts.get_area_classified()

    return df.to_json(orient='table')




@app.route("/get_sme_classified", methods=['POST'])
def get_sme_classified():

    df = ts.get_sme_classified()

    return df.to_json(orient='table')






@app.route("/get_gem_classified", methods=['POST'])
def get_gem_classified():

    df = ts.get_gem_classified()

    return df.to_json(orient='table')



@app.route("/get_st_classified", methods=['POST'])
def get_st_classified():

    df = ts.get_st_classified()

    return df.to_json(orient='table')



@app.route("/get_hs300s", methods=['POST'])
def get_hs300s():

    df = ts.get_hs300s()

    return df.to_json(orient='table')


@app.route("/get_sz50s", methods=['POST'])
def get_sz50s():

    df = ts.get_sz50s()

    return df.to_json(orient='table')




@app.route("/get_zz500s", methods=['POST'])
def get_zz500s():

    df = ts.get_zz500s()

    return df.to_json(orient='table')



@app.route("/get_terminated", methods=['POST'])
def get_terminated():

    df = ts.get_terminated()

    return df.to_json(orient='table')


@app.route("/get_suspended", methods=['POST'])
def get_suspended():

    df = ts.get_suspended()

    return df.to_json(orient='table')

#
# @app.route("/get_stock_basics", methods=['POST'])
# def get_stock_basics():
#
#     df = ts.get_stock_basics()
#
#     return df.to_json(orient='table')


@app.route("/get_report_data", methods=['POST'])
def get_report_data():

    df = ts.get_report_data(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')


@app.route("/get_profit_data", methods=['POST'])
def get_profit_data():

    df = ts.get_profit_data(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')


@app.route("/get_operation_data", methods=['POST'])
def get_operation_data():

    df = ts.get_operation_data(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')



@app.route("/get_growth_data", methods=['POST'])
def get_growth_data():

    df = ts.get_growth_data(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')

@app.route("/get_debtpaying_data", methods=['POST'])
def get_debtpaying_data():

    df = ts.get_debtpaying_data(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')

@app.route("/get_cashflow_data", methods=['POST'])
def get_cashflow_data():

    df = ts.get_cashflow_data(year=int(request.form['year']),quarter=int(request.form['quarter']))

    return df.to_json(orient='table')


@app.route("/get_deposit_rate", methods=['POST'])
def get_deposit_rate():

    df = ts.get_deposit_rate()

    return df.to_json(orient='table')



@app.route("/get_loan_rate", methods=['POST'])
def get_loan_rate():

    df = ts.get_loan_rate()

    return df.to_json(orient='table')



@app.route("/get_rrr", methods=['POST'])
def get_rrr():

    df = ts.get_rrr()

    return df.to_json(orient='table')


@app.route("/get_money_supply", methods=['POST'])
def get_money_supply():

    df = ts.get_money_supply()

    return df.to_json(orient='table')


@app.route("/get_money_supply_bal", methods=['POST'])
def get_money_supply_bal():

    df = ts.get_money_supply_bal()

    return df.to_json(orient='table')


@app.route("/get_gdp_year", methods=['POST'])
def get_gdp_year():

    df = ts.get_gdp_year()

    return df.to_json(orient='table')

@app.route("/get_gdp_quarter", methods=['POST'])
def get_gdp_quarter():

    df = ts.get_gdp_quarter()

    return df.to_json(orient='table')

@app.route("/get_gdp_for", methods=['POST'])
def get_gdp_for():

    df = ts.get_gdp_for()

    return df.to_json(orient='table')

@app.route("/get_gdp_pull", methods=['POST'])
def get_gdp_pull():

    df = ts.get_gdp_pull()

    return df.to_json(orient='table')

@app.route("/get_gdp_contrib", methods=['POST'])
def get_gdp_contrib():

    df = ts.get_gdp_contrib()

    return df.to_json(orient='table')

@app.route("/get_cpi", methods=['POST'])
def get_cpi():

    df = ts.get_cpi()

    return df.to_json(orient='table')

@app.route("/get_ppi", methods=['POST'])
def get_ppi():

    df = ts.get_ppi()

    return df.to_json(orient='table')


@app.route("/get_latest_news", methods=['POST'])
def get_latest_news():

    df = ts.get_latest_news(top=request.form['top'],show_content=request.form['show_content'])

    return df.to_json(orient='table')


@app.route("/get_notices", methods=['POST'])
def get_notices():

    df = ts.get_notices(code=request.form['code'],date=request.form['date'])

    return df.to_json(orient='table')


@app.route("/guba_sina", methods=['POST'])
def guba_sina():

    df = ts.guba_sina()

    return df.to_json(orient='table')





@app.route("/top_list", methods=['POST'])
def top_list():

    df = ts.top_list(date=request.form['date'])

    return df.to_json(orient='table')


@app.route("/cap_tops", methods=['POST'])
def cap_tops():

    df = ts.cap_tops(days=int(request.form['days']))

    return df.to_json(orient='table')



@app.route("/broker_tops", methods=['POST'])
def broker_tops():

    df = ts.broker_tops(days=int(request.form['days']))

    return df.to_json(orient='table')

@app.route("/inst_tops", methods=['POST'])
def inst_tops():

    df = ts.inst_tops(days=int(request.form['days']))

    return df.to_json(orient='table')



@app.route("/inst_detail", methods=['POST'])
def inst_detail():

    df = ts.inst_detail()

    return df.to_json(orient='table')


@app.route("/shibor_data", methods=['POST'])
def shibor_data():

    df = ts.shibor_data(year=request.form['year'])

    return df.to_json(orient='table')


@app.route("/shibor_quote_data", methods=['POST'])
def shibor_quote_data():

    df = ts.shibor_quote_data(year=request.form['year'])

    return df.to_json(orient='table')


@app.route("/shibor_ma_data", methods=['POST'])
def shibor_ma_data():

    df = ts.shibor_ma_data(year=request.form['year'])

    return df.to_json(orient='table')


@app.route("/lpr_data", methods=['POST'])
def lpr_data():

    df = ts.lpr_data(year=request.form['year'])

    return df.to_json(orient='table')

@app.route("/lpr_ma_data", methods=['POST'])
def lpr_ma_data():

    df = ts.lpr_ma_data(year=request.form['year'])

    return df.to_json(orient='table')



@app.route("/day_boxoffice", methods=['POST'])
def day_boxoffice():

    df = ts.day_boxoffice(date=request.form['date'])

    return df.to_json(orient='table')



@app.route("/month_boxoffice", methods=['POST'])
def month_boxoffice():

    df = ts.month_boxoffice(date=request.form['date'])

    return df.to_json(orient='table')



@app.route("/day_cinema", methods=['POST'])
def day_cinema():

    df = ts.day_cinema(date=request.form['date'])

    return df.to_json(orient='table')


if __name__ == "__main__":
    app.run(debug=True)
