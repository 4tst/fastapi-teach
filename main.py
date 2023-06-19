#!/usr/bin/env python3
# coding:utf-8

#
# Author: leoking
# Date: 2023-06-17 11:22:54
#LastEditTime: 2023-06-18 11:46:47
#LastEditors: leoking
# Description:
#

from typing import Union
from black import path_empty

from fastapi import FastAPI

app = FastAPI()


@app.get("/getItems")
def get_items_by_page(page: int=1, page_size: int=10):
    '''
    @description: 获取指定页的数据
    @param {int} page 当前页，从1开始
    @param {int} page_size 页大小，最大100
    @return {*}
    '''

    page = max(1, page)
    page_size = max(0, page_size)
    page_size = min(page_size, 100)

    items = list([
        {"id":1},
        {"id":2},
        {"id":3},
    ])

    # start=(page-1)*page_size
    end = page * page_size
    start = end - page_size
    
    return items[start:end]
