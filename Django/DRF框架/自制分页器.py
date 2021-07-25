# 自定义分页器
def get(self, request):
    # 获取 redis_conn对象
    redis_conn = get_redis_connection('operation')
    # 获取参数

    page = int(request.GET.get("page"))  # 页数

    page_size = int(request.GET.get("page_size"))  # 一页有几条数据
    # 获取数据
    b = []
    for k in redis_conn.hkeys('results'):
        d = redis_conn.hget('results', k)
        b.append(json.loads(d))

    # 自制分页器 ^.^
    # 本页(假如有数据)
    fanwei_min = page * page_size - page_size
    fanwei_max = page * page_size
    if b[fanwei_min:fanwei_max]:
        results = b[fanwei_min:fanwei_max]
    else:
        return Response("无效页面")
    # 上一页(假如有数据)
    page_next = page + 1
    fanwei_min_next = page_next * page_size - page_size
    fanwei_max_next = page_next * page_size
    if b[fanwei_min_next:fanwei_max_next]:
        url_next = "http://192.168.10.100:8000/operation_log/?page={}".format(int(page) + 1)
    else:
        url_next = None
    # 下一页(假如有数据)
    page_previous = page - 1
    fanwei_min_previous = page_previous * page_size - page_size
    fanwei_max_previous = page_previous * page_size
    if b[fanwei_min_previous:fanwei_max_previous]:
        url_previous = "http://192.168.10.100:8000/operation_log/?page={}".format(int(page) - 1)
    else:
        url_previous = None

    return Response({"count": len(b), "next": url_next, "previous": url_previous, "results": results})