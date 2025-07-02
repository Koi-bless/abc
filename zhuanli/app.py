from  flask import Flask, render_template, send_from_directory, request  # 已添加 request 导入
import os

import charts
from db_utils import DBUtils

app = Flask(__name__)
utils = DBUtils()


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/patent_data')
def patent_data():
    return render_template('patent_data.html')

@app.route('/patent_list')
def patent_list():
    keyword = request.args.get('keyword', '')
    if keyword:
        patent_sum = utils.get_patent_sum_by_keyword(keyword)[0]
        patent = utils.get_patent_by_keyword(keyword)
    else:
        patent_sum = utils.get_patent_sum()[0]
        patent = utils.get_patent()
    data = {
        'patent_sum': patent_sum,
        'patent': patent
    }
    return render_template('patent_list.html', data=data)


@app.route('/patent_by_province')
def patent_by_province():
    return render_template('patent_by_province.html')


@app.route('/patent_by_province_chart')
def patent_by_province_chart():
    data = utils.get_count_by_province()
    # 修改为使用整数索引
    provinces = [item[0] for item in data]
    counts = [item[1] for item in data]
    if not data:
        return "无法获取专利数据，请检查数据库连接", 500
    chart = charts.patent_province_chart((provinces, counts))
    return chart


@app.route('/province_percent')
def province_percent():
    return render_template('province_percent.html')


@app.route('/province_percent_chart')
def province_percent_chart():
    args = []
    items = utils.get_count_by_province()
    for item in items:
        args.append((item[0], item[1]))
    return charts.province_percent_chart(args)


@app.route('/patent_mapl')
def patent_map():
    return render_template('patent_map.html')


@app.route('/patent_map_chart')
def patent_map_chart():
    args = []
    items = utils.get_count_by_province()
    for item in items:
        args.append((item[0],item[1]))
    return charts.patent_map_chart(args)

if __name__ == '__main__':
    app.run(debug=True)