from pyecharts.charts import Bar, Pie, Map, Geo
from pyecharts import options as opts

#柱状图：
def patent_province_chart(args):
    chart = Bar()
    chart.add_xaxis(args[0])
    print(args[0])
    chart.add_yaxis('专利数量', args[1],bar_width=15)
    chart.set_global_opts(
        xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            rotate=45,  # 标签旋转45度，避免重叠
            interval=0,  # 显示所有标签（0表示不间隔）
            font_size=8  # 设置较小的字体大小
        )),
        legend_opts=opts.LegendOpts(
            is_show=False
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            max_=8686354
        )
    )
    return chart.dump_options_with_quotes()

#饼状图
def province_percent_chart(args):
    chart = Pie()
    chart.add(
        series_name="各省占比",
        data_pair=args,
        radius=["40%", "75%"],  # 饼图的内外半径
    )
    chart.set_global_opts(
        legend_opts=opts.LegendOpts(
            pos_right='5%',
            pos_top='middle',
            orient='vertical'
        )
    )
    chart.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    return chart.dump_options_with_quotes()

#热点图
def patent_map_chart(args):
    chart = Map()
    chart.add(
        series_name="专利热点图",
        data_pair=args,
        maptype='china',
        zoom = 1.5
    )
    chart.set_global_opts(
        title_opts=opts.TitleOpts(
            title="全国专利分布",
            pos_right='center',
            pos_top='5%'
        ),
        visualmap_opts=opts.VisualMapOpts(
            max_=8686514,
            min_=1434,
            range_color=['#1E9600','#FFF200','#FF0000']
        ),
        legend_opts=opts.LegendOpts(
            pos_right='10%',
            pos_top='middle',
            orient='vertical',
            is_show=False
        )
    )
    return chart.dump_options_with_quotes()
