local link_id = redis.call("INCR", KEYS[1])
redis.call("HSET", link_id, KEYS[2], ARGV[1])
return link_id
