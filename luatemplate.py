#!/usr/bin/env python
# coding: utf-8

import redis

rds = redis.Redis()

lpush = """
    local data = {
    % for datum in data:
        '${ ujson.dumps(datum) }',
    % endfor
    }

    for k, v in pairs(data) do
        redis.call('lpush', '${ name }', v)
    end
"""

lpop = """
    local name = KEYS[1]
    local length = KEYS[2]
    if length == -1 then
        length = redis.call('llen', name)
    end
    local t = {}
    for i=1, length, 1 do
        table.insert(t, redis.call('lpop', name))
    end
    return t
"""

hset = """
    local name = KEYS[1]
"""


lpush_sha = rds.script_load(lpush)
lpop_sha = rds.script_load(lpop)


print rds.evalsha(lpush_sha, 0)
print rds.evalsha(lpop_sha, 0)