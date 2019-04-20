#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Hongzhi Cao'

import orm
import asyncio,random,string
from models import User, Blog, Comment,next_id


async def test(loop):
    await orm.create_pool(loop=loop, user='caohz', password='ahooge123', db='caohz_blog')

    u = User(name='test', email='12345678@qq.com', passwd='123456', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
for x in test(loop):
    pass