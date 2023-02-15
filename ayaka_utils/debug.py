import inspect


def debug_print(*args):
    '''快速插桩'''
    t = inspect.stack()[1]
    items = [
        "---- debug_print ----",
        f"File \"{t.filename}\", line {t.lineno}, when running",
        t.code_context[0].rstrip()
    ]
    print("\n".join(items))
    print(*args, "\n")


def simple_repr(obj: object, exclude: set[str] = set(), **params):
    '''快速获得一份简单的对象repr

    参数：

        obj：对象

        exclude：不展示该对象的一些属性

        params：使用指定值覆盖该对象的一些属性（不修改对象值）

            该参数在一些属性的默认str不便于展示时尤为好用，可以自己设置该属性的展示值，例如：

            simple_repr(a, func=a.func.__name__)

            其展示的func属性则为str(a.func.__name__)而非str(a.func)
    '''
    # 复制一份，防止update修改原内容
    data = {k: v for k, v in vars(obj).items() if k not in exclude}
    data.update(params)
    data = ", ".join(f"{k}={v}" for k, v in data.items())
    return f"{obj.__class__.__name__}({data})"
