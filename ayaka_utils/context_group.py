'''上下文'''
from contextvars import ContextVar
from .utils import Undefined

context_dict: dict[str, ContextVar] = {}


class FieldInfo:
    def __init__(self, default, default_factory, exclude) -> None:
        self.default = default
        self.default_factory = default_factory
        self.exclude = exclude

    def create_prop(self, name: str):
        if self.default is not Undefined:
            context = ContextVar(name, default=self.default)
        else:
            context = ContextVar(name)

        context_dict[name] = context

        if self.default is Undefined and self.default_factory is not Undefined:
            def fget(_self):
                try:
                    return context.get()
                except LookupError:
                    s = self.default_factory()
                    context.set(s)
                    return s

        else:
            def fget(_self):
                return context.get()

        def fset(_self, v):
            context.set(v)

        prop = property(
            fget=fget,
            fset=fset
        )

        return prop


def Field(default=Undefined, default_factory=Undefined, exclude=False):
    return FieldInfo(
        default=default,
        default_factory=default_factory,
        exclude=exclude
    )


class ContextGroup:
    def __new__(cls):
        for key in cls.__annotations__.keys():
            # 跳过特殊名称
            if key.startswith("_"):
                continue

            # 生成FieldInfo
            if hasattr(cls, key):
                value = getattr(cls, key)
                if not isinstance(value, FieldInfo):
                    value = Field(default=value)
            else:
                value = Field()

            if value.exclude:
                continue

            name = f"{cls.__name__}_{key}"

            # 替换为property
            setattr(cls, key, value.create_prop(name))

        return super().__new__(cls)
