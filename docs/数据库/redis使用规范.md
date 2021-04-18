# redis 最佳实践

## 使用规范

### 内存控制

- 控制 key 的长度
- 避免存储 bigkey
- 选择合适的数据类型
  - string、set 存储 int 类型数据
  - hash、zset 控制存储元素的数量
- 尽量把redis当成缓存使用，而不是数据库
- 设置 maxmemory + 淘汰策略
- 如果可以压缩数据，把数据压缩后写入redis（但是解压或消耗更多的CPU资源）

### 高性能

- 避免存储 bigkey
- 开启 lazy-free 机制
- 不使用复杂度过高的命令
  - sort
  - sinter
  - sinterstore
  - zunionstore
  - zinterstore
- 执行 O(N) 命令时，注意 N 的大小
- 注意 DEL 时间复杂度
  - 删除的 key 是 list/hash/set/zset 类型时，复杂度是 O(N)
  - list类型：多次执行 LPOP/RPOP
  - hash/set/zset类型：先执行 HSCAN/SSCAN/SCAN 查询元素，再执行 HDEL/SREM/ZREM 依次删除每个元素
- 批量命令代替单个命令
  - MGET/MSET 替代 GET/SET，HMGET/HMSET 替代 HET/HSET
  - 使用 pipeline，打包多个命令
- 避免集中过期 key
- 使用长连接操作 redis，合理配置连接池
- 关闭操作系统内存大页机制
- 禁止使用 KEYS/FLUSHALL/FLUSHDB

### 安全性

- 不要部署在公网可访问的服务器上
- 不要使用默认端口 6379
- 以普通用户启动 redis 进程，禁止 root 用户启动
- 限制 redis 配置文件的目录访问权限
- 开启密码认证
- 禁止/重命名危险命令（KEYS/FLUSHALL/FLUSHDB/CONFIG/EVAL）

## 常用命令

详见：http://redisdoc.com/

