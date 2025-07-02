from DrissionPage import ChromiumOptions, ChromiumPage
import time
import pymysql
import random

options = ChromiumOptions()
dp = ChromiumPage(options)


def write_to_mysql():
    connect = None
    try:
        # 关键词列表
        keywords = [
                '计算机', '人工智能', '物理', '医学', '数学', '生物学', '电子', '通信',
                '化学', '材料科学', '机械工程', '环境科学', '能源', '航空航天', '农业', '食品科学',
                '生物技术', '纳米技术', '机器人', '物联网', '大数据', '云计算', '5G', '量子计算',
                '基因编辑', '制药', '医疗器械', '半导体', '光电子', '汽车工程'
        ]
        # 数据库连接
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            database='zhuanli',
            charset='utf8mb4'
        )
        cursor = conn.cursor()

        for kw in keywords:
            print(f'正在采集关键词：{kw}')
            url = f'https://kns.cnki.net/kns8s/search?classid=VUDIXAIY&kw={kw}&korder=SU&language=CHS&uniplatform=NZKPT'
            dp.get(url)
            dp.wait.load_start()
            time.sleep(2)
            page_count = 0
            while page_count < 8:
                page_count += 1
                print(f'正在采集关键词【{kw}】第{page_count}页...')
                dp.wait.load_start()
                time.sleep(random.uniform(2, 4))

                # 采集表格行
                rows = dp.eles('css:table.result-table-list tbody tr')
                print(f'本页找到{len(rows)}条专利')
                for row in rows:
                    try:
                        # 专利名称
                        title_ele = row.ele('css:td.name a.fz14')
                        title = title_ele.text if title_ele else ''
                        # 发明人
                        inventor_eles = row.eles('css:td.inventor a')
                        inventors = ';'.join([a.text for a in inventor_eles]) if inventor_eles else ''
                        # 申请人
                        applicant_ele = row.ele('css:td.applicant')
                        applicant = applicant_ele.text if applicant_ele else ''
                        # 数据库
                        database_ele = row.ele('css:td.data')
                        database = database_ele.text if database_ele else ''
                        # 申请日、公开日
                        date_eles = row.eles('css:td.date')
                        apply_date = date_eles[0].text if len(date_eles) > 0 else ''
                        public_date = date_eles[1].text if len(date_eles) > 1 else ''
                        print(f'专利名称: {title} | 发明人: {inventors} | 申请人: {applicant} | 数据库: {database} | 申请日: {apply_date} | 公开日: {public_date} | 关键词: {kw}')
                        # 插入数据库
                        sql = """
                            INSERT INTO patent_info (title, famingren, quanren, database_name, shenqingri, gonggaori, keyword)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(sql, (title, inventors, applicant, database, apply_date, public_date, kw))
                        conn.commit()
                    except Exception as e:
                        print('采集专利信息失败:', e)
                # 翻页
                next_btn = None
                for btn in dp.eles('css:a.pagesnums'):
                    if btn.text.strip() == '下一页':
                        next_btn = btn
                        break
                if next_btn:
                    try:
                        next_btn.click()
                        time.sleep(random.uniform(2, 4))
                    except Exception as e:
                        print('点击下页失败:', e)
                        break
                else:
                    print('已到最后一页或未找到下一页按钮，采集结束。')
                    break

        cursor.close()
        conn.close()
        dp.close()
        print('采集完成')
    except Exception as e:
        print(e)
        connect.rollback()
    finally:
        if connect:
            connect.close()


if __name__ == "__main__":
    write_to_mysql()