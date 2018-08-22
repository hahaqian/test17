from redis import *

def use_redis():

    try:
            # 创建StrictRedis对象，与redis服务器建⽴连接
            redis = StrictRedis(decode_responses=True)

            # 添加键name，值为itheima
            redis.set("name","itheima")

            # 输出响应结果，如果添加成功则返回True，否则返回False
            print(redis.get("name"))

    except Exception as e:
         print(e)



"""
配置集群：
redis-trib.rb create --replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005


"""



if __name__ == '__main__':
    use_redis()