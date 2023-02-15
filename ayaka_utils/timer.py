from time import time


class Timer:
    '''计时器

    示例代码:
    ```
        with Timer("test"):
            # some code...

        # 输出：[test] 耗时2.02s
    ```
    '''

    def __init__(self, name: str = "", show: bool = True, formater=lambda x: f"{x:.2f}s") -> None:
        self.name = name
        self.diff = 0
        self.show = show
        self.formater = formater

    def __enter__(self):
        self.time = time()

    def __exit__(self, a, b, c):
        self.diff = time() - self.time
        if self.show:
            print(f"[{self.name}] 耗时{self.formater(self.diff)}")
