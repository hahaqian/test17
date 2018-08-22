from rediscluster import  StrictRedisCluster

def use_cluster():

    # 设置uabntud的桥接ip地址即可
    startup_nodes =[
        {"host": "192.168.75.132", "post": 7001},
        {"host": "192.168.75.132", "post": 7002},
        {"host": "192.168.75.132", "post": 7003},

    ]

    # 1.创建集群对象
    cluster = StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)

    # 2.设置值
    cluster.set("name","laowang")

    # 3.获取值
    print(cluster.get("name"))

    # ceshi

if __name__ == '__main__':
    use_cluster()