# redis充当分布式锁

将 redis 作为分布式锁使用的时候，一般有下面几种方案：

- SETNX + EXPIRE
- SETNX + value 值
- 使用 lua 脚本（SETNX + EXPIRE）
- SET 的扩展命令（SET EX PX NX）
- SET EX PX NX + 校验唯一随机值，再释放锁
- Redisson
- 多机分布式锁 Redlock

## 什么是分布式锁

- 互斥性：任意时刻，只有一个客户端能持有锁
- 锁超时释放：持有锁超时，可以释放，防止死锁
- 可重入：一个线程获取了锁之后，可以再次对其请求加锁
- 高可用，高性能：加解锁的开销尽可能低，同时也要保证高可用
- 安全性：锁只能被持有的客户端删除，不能被其他客户端删除

### SETNX + EXPIRE

> SETNX 是 SET IF NOT EXISTS 的简写，命令格式：SETNX key value，如果 key 不存在，则 SETNX  成功返回 1，如果 key 已存在，返回 0。

可以先用 `SETNX` 抢锁，抢到之后再用 `EXPIRE` 给锁设置一个过期时间，防止忘记释放锁。

大概的伪代码：

```python
if redis.setnx(lock_key, lock_value) == 1:
    redis.expire(lock_key, 100)  # 设置过期时间
    try:
        do_something()
    finally:
        redis.del(lock_key)
```

但是这个方案中，`setnx` 和 `expire` 两个命令分开执行了，**不是原子操作**。如果执行完 `setnx` 之后，还没来得及执行 `expire` 系统奔溃或者重启，那么这个锁将永远存在，后续**永远无法获取锁了。**

### SETNX + value 值





