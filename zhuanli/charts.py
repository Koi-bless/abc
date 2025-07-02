from pyecharts.charts import Bar, Pie, Map, Geo, Line
from pyecharts import options as opts
import numpy as np
from pyecharts.commons.utils import JsCode

#柱状图：
def patent_province_chart(args):
    chart = Bar()
    chart.add_xaxis(args[0])
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

#预测
def prediction_line():  
    years = [
        1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994,
        1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,
        2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
    ]

    patents = [
        0.1, 0.7, 1.3, 2.1, 2.7, 2.6, 3.4, 4.8, 4.0, 5.2,
        4.9, 5.0, 5.6, 6.7, 10.0, 11.0, 12.3, 14.2, 18.4, 19.6,
        24.6, 30.5, 40.8, 50.1, 66.1, 92.9, 111.4, 156.5, 184.9, 187.7,
        243.5, 259.8, 286.0, 369.6, 382.7, 485.2, 601.8, 573.2, 492.0, 656.3
    ]

    # 创建年份偏移量（以1985年为基准）
    x = [year - 1985 for year in years]

    # 三次多项式拟合
    degree = 3
    coeffs = np.polyfit(x, patents, degree)
    poly = np.poly1d(coeffs)

    # 生成拟合曲线
    x_fit = list(range(0, 42))  # 1985-2026
    y_fit = poly(x_fit)
    fit_years = [1985 + i for i in x_fit]

    # 预测2025和2026年
    x_2025 = 2025 - 1985
    x_2026 = 2026 - 1985
    pred_2025 = poly(x_2025)
    pred_2026 = poly(x_2026)
    
    # 创建图表实例
    line = Line(init_opts=opts.InitOpts(
        width="1200px",
        height="1000px",
        theme="white",
        bg_color="#f8f9fa"
    ))

    line.add_xaxis(xaxis_data=fit_years)  # 使用完整年份范围作为X轴
    
    # 实际数据点（只显示有数据的年份）
    line.add_yaxis(
        series_name="实际专利数量",
        y_axis=[patents[i] if year in years else None for i, year in enumerate(fit_years[:len(years)])],
        symbol="circle",
        symbol_size=8,
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3, color="#5470C6"),
        itemstyle_opts=opts.ItemStyleOpts(color="#5470C6")
    )
    
    # 拟合曲线
    line.add_yaxis(
        series_name="拟合曲线",
        y_axis=y_fit.tolist(),
        symbol="none",
        is_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3, color="#91CC75", type_="dashed"),
        itemstyle_opts=opts.ItemStyleOpts(color="#91CC75")
    )
    
    # 预测点
    line.add_yaxis(
        series_name="预测值",
        y_axis = [None] * (len(fit_years) - 2) + [pred_2025, pred_2026],  # 只在最后两个点显示预测值
        symbol="diamond",
        symbol_size=16,

        label_opts=opts.LabelOpts(
            position="top",
            color="#EE6666",
            font_size=14,
            font_weight="bold"
        ),

        linestyle_opts=opts.LineStyleOpts(width=0),
        itemstyle_opts=opts.ItemStyleOpts(color="#EE6666")
    )

    # 设置全局配置
    line.set_global_opts(
        title_opts=opts.TitleOpts(
            title="中国申请专利数量增长趋势与预测 (1985-2026)",
            subtitle="基于三次多项式拟合模型",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=24,
                font_weight="bold",
                color="#333"
            ),
            subtitle_textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                color="#666"
            )
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            formatter=JsCode(
                """function(params) {
                    var value = params[0].value;
                    var seriesName = params[0].seriesName;
                    var year = value[0];
                    var patent = value[1];
                    
                    if (seriesName === '预测值' && patent !== null) {
                        return year + '年预测: ' + patent.toFixed(1) + '万件';
                    } else if (seriesName === '实际专利数量' && patent !== null) {
                        return year + '年: ' + patent.toFixed(1) + '万件';
                    } else if (seriesName === '拟合曲线' && patent !== null) {
                        return year + '年拟合值: ' + patent.toFixed(1) + '万件';
                    }
                    return '';
                }"""
            ),
            axis_pointer_type="line"
        ),
       
        xaxis_opts=opts.AxisOpts(
            type_="value",  # 改为数值轴
            name="年份",
            name_location="end",
            name_gap=20,
            name_textstyle_opts=opts.TextStyleOpts(font_size=14),
            axislabel_opts=opts.LabelOpts(
                formatter="{value}年",
                font_size=12
            ),
            min_=1985,
            max_=2026,
            interval=5,  # 每5年一个刻度
            splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="专利申请数量 (万件)",
            name_location="end",
            name_gap=40,
            name_textstyle_opts=opts.TextStyleOpts(font_size=14),
            axislabel_opts=opts.LabelOpts(
                formatter="{value}",
                font_size=12
            ),
            splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        legend_opts=opts.LegendOpts(
            pos_top="5%",
            pos_right="5%",
            orient="vertical",
            item_gap=20,
            textstyle_opts=opts.TextStyleOpts(font_size=14)
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                type_="inside",
                range_start=70,
                range_end=100
            ),
            opts.DataZoomOpts(
                type_="slider",
                pos_bottom="5%",
                range_start=0,
                range_end=100
            )
        ],
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            pos_left="right",
            pos_top="top",
            feature={
                "saveAsImage": {},
                "restore": {},
                "dataView": {"readOnly": False},
                "dataZoom": {},
                "magicType": {"type": ["line", "bar"]}
            }
        )
    )

    # 添加特殊点标注
    line.set_series_opts(
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(
                    name="2023年异常点",
                    coord=[2023, 492],
                    value=492,
                    symbol="pin",
                    symbol_size=50,
                    itemstyle_opts=opts.ItemStyleOpts(color="#FF0000"),
                )
            ]
        )
    )

    # 添加拟合方程文本
    equation_text = f"拟合方程: y = {coeffs[0]:.5f}x³ + {coeffs[1]:.4f}x² + {coeffs[2]:.4f}x + {coeffs[3]:.2f}"
    line.set_global_opts(
        graphic_opts=[
            opts.GraphicText(
                graphic_item=opts.GraphicItem(
                    left="center",
                    top="bottom",
                    z=100
                ),
                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                    text=equation_text,
                    font="14px Microsoft YaHei",
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill="#333"
                    )
                )
            )
        ]
    )

    # 添加预测值标注
    line.set_series_opts(
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(
                    name="2025预测",
                    coord=[2025, pred_2025],
                    value=pred_2025,
                    symbol="circle",
                    symbol_size=10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#EE6666")
                ),
                opts.MarkPointItem(
                    name="2026预测",
                    coord=[2026, pred_2026],
                    value=pred_2026,
                    symbol="circle",
                    symbol_size=10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#EE6666")
                )
            ]
        )
    )

    return line.dump_options_with_quotes()
