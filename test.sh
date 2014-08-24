#!/bin/bash

rsync -avzh ubuntu@183.60.243.217:/data/gacdata/20140527/ /downloads/Downloads/

# 测试说明rsync也是shell进程阻塞的
while $(pidof scp); do
    sleep 5
    echo "Sleeping"
done

echo "下载成功"
