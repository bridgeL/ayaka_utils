import asyncio
import functools


def is_async_callable(obj) -> bool:
    '''抄自 starlette._utils.is_async_callable

    判断对象是否可异步调用'''
    while isinstance(obj, functools.partial):
        obj = obj.func

    return asyncio.iscoroutinefunction(obj) or (
        callable(obj) and asyncio.iscoroutinefunction(obj.__call__)
    )


def simple_async_wrap(func):
    '''简单将一个同步函数表面上转为异步'''
    async def async_func(*args, **kwargs):
        func(*args, **kwargs)
    return async_func
