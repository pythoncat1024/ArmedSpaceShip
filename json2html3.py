# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     html
   Description :
   Author :       cat
   date：          2018/3/6
-------------------------------------------------
   Change Activity:
                   2018/3/6:
-------------------------------------------------
"""
import json
from os import getcwd
from codecs import open


def _power_write_html_from_str(html_name, html_str):
    f = open(html_name, 'w', encoding='utf-8')
    f.write(html_str)
    f.close()

    print("write 2 [", html_name, "] ok")


def power_do_something():
    import logging
    # 0. 读 json , 按行过滤 短 {} , 生成 [{},{},{}]
    # 0.5 添加一行 jira_id  # todo: important
    # 1. 移除不展示的 key
    # 1.1 将 owner 子串 替换成 owner_username , owner_email
    # 1.5 读取 template.html的内容，存储为 字符串
    # 2. 获取 {}.keys()  ===>[全部是需要展示的了]
    # 3. 做一个映射 --> (subject:jiraID, project:xxx),根据映射生成 thead 内容 [模板+映射后]
    # 4. 根据 {}.keys() 生成 tbody 的 内容
    # 5. 写入全部内容到 power_html.html

    ################################################
    # step 0: 读 json , 按行过滤 短 {} , 生成 [{},{},{}]
    data = _power_read_json_data('commit.json')  # --> [{},{}]
    # ['project', 'branch', 'id', 'number', 'subject', 'owner', 'url',
    #  'commitMessage', 'createdOn', 'lastUpdated', 'open', 'status']

    # step 1: 移除 不展示的 key
    useful = ['subject', 'owner', 'url']
    for item in data:
        keys = dict(item).keys()
        # step 0.5 添加 一条 jira_id
        item['jira_id'] = _power_parse_jira_id_from_subject(dict(item).get('subject'))
        for key in keys:
            if key not in useful:
                item.pop(key)
            elif key == 'owner':
                # step 1.1 将 owner 子串 替换成 owner_username , owner_email
                owner = item.pop(key)
                item[key + '_username'] = owner.get('username')

    # step 1.5:  读取 template.html的内容，存储为 字符串
    import os
    html_template_str = _power_read_html_template(
         'power_template.html')

    # step 2: 获取 {}.keys()  ===>[全部是需要展示的了]
    titles = data[0].keys()
    logging.error(titles)

    # step 3: 做一个映射 --> (subject:jiraID, project:xxx),根据映射生成 thead 内容 [模板+映射后]
    # step 3: 映射 [list_titles_origin] --> [list_titles_friendly] --> thead 内容插入完成
    power_titles = _power_titles(titles)
    html_template_str = _power_insert_tr_in_thead(html_template_str, power_titles)

    # step 4: 根据 {}.keys() 生成 tbody 的 内容
    html_source = _power_insert_tr_in_tbody(html_template_str, data)
    # step 5. 写入全部内容到 power_html.html
    _power_write_html_from_str('lastReleaseNote.html', html_source)

    pass


def _power_parse_jira_id_from_subject(subject_str):
    """
    从 subject 中 解析出 jira_id
    :param subject_str:
    :return:
    """
    import re
    match_list = re.findall("\[[A-Z0-9]+-[0-9]+\]", subject_str)
    #  [] , ['[GM3F-149]']
    # print("JIRAID==", match_list)
    if not match_list:
        return "NA"
    else:
        return ",".join(list(map(lambda ee: ee.replace("[", "").replace("]", ""), [ele for ele in match_list])))


def _power_insert_tr_in_tbody(html_str, dict_list):
    """
    插入 数据到 <tbody> 中
    :param html_str:
    :param dict_list: [{},{},{}] ,每个元素是一条数据
    :return: 插入后的 html_str
    """
    tb = "<tbody>"
    start = str(html_str).index(tb) + len(tb)

    head = html_str[0:start]  # ... <tbody>
    tail = html_str[start:len(html_str)]  # </tbody> ...
    tr_items = _power_create_tr_items_for_tbody(dict_list)
    html_source = head + tr_items + tail
    # print("insert_tr_in_tbody:%s" % html_source)
    return html_source


SHOW_URL = True


def _power_create_tr_items_for_tbody(dict_list):
    """
    # 'subject', 'url'
    :param dict_list:  [{},{},{}]
    :return:
    """
    tr_items = ""
    for item in dict_list:
        tr_items += "\n<tr>\n"
        td = "<td>"
        tde = "</td>\n"
        # r'<a href="{}" target="_blank">'
        aleft = r'<a href="{}">'.format(item.get('url'))
        aright = r"</a>"
        for key in item.keys():
            if 'subject' == key:
                tr_items += td + aleft + item.get(key) + aright + tde

                _power_parse_jira_id_from_subject(item.get(key))
            elif 'url' == key:
                pass
            else:
                tr_items += td + str(item.get(key)) + tde
        tr_items += "</tr>"

    # print("create_tr_items_for_tbody: %s" % tr_items)

    return tr_items


def _power_insert_tr_in_thead(html_str, power_titles):
    """
    插入 一行 <tr><td>aaa</td> <td>bbb</td> </tr> 到 html_str 中
    :param html_str:  html_str
    :param power_titles:  ['SUBJECT', 'URL', 'STATUS', 'OWNER_USERNAME', 'OWNER_EMAIL']
    :return:  插入后的 html_str
    """
    # 插入 thead 的实际内容 ['SUBJECT', 'URL', 'STATUS', 'OWNER_USERNAME', 'OWNER_EMAIL']
    # 前面加一个 BUG_ID
    th = "<thead>"
    start = str(html_str).index(th) + len(th)
    # print("################################################### start %d" % start)
    head = html_str[0:start]  # ... <thead>
    tail = html_str[start:len(html_str)]  # </thead> ...
    # print("thead---> head and tail", head, tail)
    tr_item = ""
    tr_item += "\n<tr>\n"
    td = "<td>"
    tde = "</td>\n"
    for title in power_titles:
        tr_item += td + title + tde
        pass
    tr_item += "</tr>"

    html_source = head + tr_item + tail
    # print("insert_tr_in_thead%s" % html_source)
    # write_html_from_str('power_html.html', html_source)
    return html_source


def _power_read_html_template(html_file):
    """
    读取模板 html 文件 (template.html) 的全部内容
    :param html_file: template.html
    :return: template.html 的内容
    """
    html_str = open(html_file, "r", encoding="utf-8").read()
    return html_str


def _power_titles(titles):
    """
    将 ['subject', 'url', 'status', 'owner_username', 'owner_email'] 转化成 友好的 titles
    :param titles: ['subject', 'url', 'status', 'owner_username', 'owner_email']
    :return: ['SUBJECT', 'URL', 'STATUS', 'OWNER_USERNAME', 'OWNER_EMAIL'] 或者其他的
    """
    p_titles = [title.upper() for title in titles if title != 'url']
    return p_titles


def _power_read_json_data(json_file):
    """
    将一个 xxx.json 的文件转成一个 [{},{}]  list 里面每个元素是一个 dict
    # 按行读取，每一行是一个 json 字符串 ，所以，每一行是一个 dict
    :param json_file: xxx.json
    :return: [{},{}]  list
    """
    f = open(json_file, 'r', encoding='UTF-8')

    dict_list = [json.loads(line) for line in f if 'branch' in line and "project" in line]
    f.close()
    return dict_list


if "__main__" == __name__:
    # run()

    # #############  ok ---- html--------
    # html_template = read_html_template('template.html')
    # last = insert_tr(html_template, 3)
    # print(last)
    # #############  ok ---- html--end--------

    # read_json_data('commit.json')

    # do_something()
    power_do_something()
    pass
