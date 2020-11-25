#! --UTF-8 --

import requests
import time, re
import json
from lxml import etree
from bs4 import BeautifulSoup
# import pandas as pd
import xlwt
from selenium import webdriver
from com.jensen.spider.settings import BaseInfo


def log(show_info):
    print(show_info)


class Spider:
    __instance = None

    def __init__(self):
        pass

    def formatText(self, text):
        if text is None:
            return None
        return text.replace('\n', '').replace('  ', '')

    def getResponse(self, site, area, page_str):
        url = site['url'].format(area, page_str)
        headers = site['headers']
        return requests.get(url, headers=headers)

    def regData(self, pattern, text):
        if len(pattern.strip()) < 4 or text is None:
            return None
        line = re.search(pattern, text, re.M | re.I)
        if line is None:
            return None
        return line.group()

    def bs_parse(self, data_list, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        items = soup.find_all('li', class_='clear')
        # print('data=', len(items))
        for item in items:
            # print('item', item)
            title = item.find('div', attrs={'class', 'title'}).a.text
            new_flag = item.find('div', attrs={'class', 'title'}).span
            if new_flag is not None:
                title = title + " [" + new_flag.text + "] "
            title_href = item.find('div', attrs={'class', 'title'}).a['href']
            house_action = item.find('div', attrs={'class', 'title'}).a['data-action']
            house_id_flag = self.regData(r'housedel_id=(\d{12})&', house_action)
            house_id = None
            if house_id_flag is not None:
                house_id = str(self.regData(r'(\d{12})', house_id_flag))
            # print('title = ', title, house_id)
            address = item.find('div', attrs={'class', 'positionInfo'}).a.text
            address_href = item.find('div', attrs={'class', 'positionInfo'}).a['href']
            house_info = self.formatText(item.find('div', attrs={'class', 'houseInfo'}).text)
            follow_info = self.formatText(item.find('div', attrs={'class', 'followInfo'}).text)
            tags = item.find('div', attrs={'class', 'tag'}).find_all('span')
            # print(tags)
            tag_list = []
            for tag in tags:
                tag_list.append(tag.text)
            price = item.find('div', attrs={'class', 'totalPrice'}).span.text
            price_unit = item.find('div', attrs={'class', 'totalPrice'}).text
            unit_price = item.find('div', attrs={'class', 'unitPrice'}).span.text
            data_list.append({
                'house_id': house_id,
                'title': title,
                'title_href': title_href,
                'house_info': house_info,
                'tags': "|".join(tag_list),
                'price': float(price),
                'price_unit': price_unit,
                'unit_price': unit_price,
                'follow_info': follow_info,
                'address': address,
                'address_href': address_href
            })
        # print(data_list)
        print(len(data_list))
        return data_list

    def xpath_parse(self, data_list, response, site):
        path = site['xpath']
        content = etree.HTML(response.text)
        time.sleep(5)
        results = content.xpath(path)
        print(results)
        for result in results:
            items = result.xpath('./a/div/p')
            title = None
            house_info = None
            house_more = []
            price = None
            for i, item in enumerate(items):
                if i in (0, 1, 3):
                    item_text = item.xpath('./text()')
                    if len(item_text) > 0:
                        format_str = self.formatText(item_text[0])
                        if i == 0:
                            title = format_str
                        elif i == 1:
                            house_info = format_str
                        else:
                            price = format_str
                if i == 2:
                    i_text = item.xpath('./i')
                    for i_str in i_text:
                        house_more.append(i_str.xpath('./text()'))
            print(title, house_info, house_more, price)

            date_time = time.strftime("%Y-%m-%d", time.localtime())
            """数据存入字典"""
            data_dict = {
                "date_time": date_time
            }
            # print(data_dict)

    def selenium_parse(self, site):
        driver = webdriver.Chrome()
        driver.get(site['url'])
        div_text = driver.find_element_by_css_selector('#root > div > div.container > div.ershoufang-page__list-area > div.kem__list-tile.am-list-view-scrollview > div.am-list-body > div > div:nth-child(1) > a > div > div.house-text > div.house-title').text
        print(div_text)

    def run(self, site=None, method='bs', area='dashiba'):
        data_list = []
        for pageno in [1, 2, 3, 4, 5]:
            page_str = ''
            if pageno > 1:
                page_str = 'pg{}'.format(pageno)
            response = self.getResponse(site, area, page_str)
            if response.status_code != 200:
                return
            if method == 'xpath':
                self.xpath_parse(data_list, response, site)
            else:
                self.bs_parse(data_list, response)
        return data_list


def write_excel(area_name, list_date):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 写入excel
    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(0, 0, 'house_id')
    worksheet.write(0, 1, 'title')
    worksheet.write(0, 2, 'title_href')
    worksheet.write(0, 3, 'house_info')
    worksheet.write(0, 4, 'tags')
    worksheet.write(0, 5, 'price')
    worksheet.write(0, 6, 'price_unit')
    worksheet.write(0, 7, 'unit_price')
    worksheet.write(0, 8, 'follow_info')
    worksheet.write(0, 9, 'address')
    worksheet.write(0, 10, 'address_href')
    for _i, line in enumerate(list_date):
        i = _i + 1
        worksheet.write(i, 0, line['house_id'])
        worksheet.write(i, 1, line['title'])
        worksheet.write(i, 2, line['title_href'])
        worksheet.write(i, 3, line['house_info'])
        worksheet.write(i, 4, line['tags'])
        worksheet.write(i, 5, line['price'])
        worksheet.write(i, 6, line['price_unit'])
        worksheet.write(i, 7, line['unit_price'])
        worksheet.write(i, 8, line['follow_info'])
        worksheet.write(i, 9, line['address'])
        worksheet.write(i, 10, line['address_href'])

    # 保存
    workbook.save('C:\\Users\\Jensen\\Desktop\\{}.xls'.format(area_name))


if __name__ == '__main__':
    log('Start')
    site_name = 'ke'
    site = BaseInfo.SITES[site_name]
    mySpider = Spider()
    for area_name in BaseInfo.area_dict.keys():
        area_name_en = BaseInfo.area_dict[area_name]
        dict_data = mySpider.run(site=site, method='bs', area=area_name_en)
        # df = pd.DataFrame.from_dict(dict_data, orient='index', columns=['house_id'])
        # print(df)
        write_excel(area_name, dict_data)
        log('完成[{}]区域数据爬取！'.format(area_name))

    log('End')

