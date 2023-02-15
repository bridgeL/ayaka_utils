class UndefinedType:
    pass


Undefined = UndefinedType()


def singleton(cls):
    '''单例模式的装饰器'''
    result = None
    done = False

    def getinstance(*args, **kwargs):
        nonlocal result, done
        if not done:
            done = True
            result = cls(*args, **kwargs)
        return result

    return getinstance


def ensure_list(data: str | list | tuple | set):
    '''确保为列表'''
    if isinstance(data, str):
        return [data]
    if isinstance(data, list):
        return data
    return list(data)


async def do_nothing():
    '''什么也不做，可以当个占位符'''
    pass
