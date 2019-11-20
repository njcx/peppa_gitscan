# peppa_gitscan
一款可以自动获取代理的高性能github 扫描器


#### 介绍

- 支持github多账户
- 多进程+协程（分钟级发现）
- 自动获取代理
- 匹配链
- 封了自动换账户，换代理

#### 安装

```bash 

# docker run -d --name myredis -p 6379:6379 redis --requirepass "test" 

# docker run -d --env db_type=REDIS --env db_host=10.10.23.68 --env db_port=6379 --env db_password=test -p 127.0.0.1:5010:5010 jhao104/proxy_pool 

# db_host 和 db_password， db_port  按实际情况修改

```

代理使用的是 

https://github.com/jhao104/proxy_pool

致谢



![我是一个图片](https://raw.githubusercontent.com/njcx/peppa_gitscan/master/doc/images/1574238292100.jpg)

