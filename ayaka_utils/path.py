import json
from pathlib import Path


def ensure_dir_exists(path: str | Path):
    '''确保目录存在

    参数：

        path：文件路径或目录路径

            若为文件路径，该函数将确保该文件父目录存在

            若为目录路径，该函数将确保该目录存在

    返回：

        Path对象
    '''
    if not isinstance(path, Path):
        path = Path(path)
    # 文件
    if path.suffix:
        ensure_dir_exists(path.parent)
    # 目录
    elif not path.exists():
        path.mkdir(parents=True)
    return path


def load_data_from_file(path: str | Path):
    '''从指定文件加载数据

    参数:

        path: 文件路径（ayaka会自动确保路径存在）

        若文件类型为json，按照json格式读取

        若文件类型为其他，则按行读取，并排除空行

    返回:

        json反序列化后的结果(对应.json文件) 或 字符串数组(对应.txt文件)
    '''
    path = ensure_dir_exists(path)
    if not path.exists():
        raise Exception(f"文件不存在 {path}")

    with path.open("r", encoding="utf8") as f:
        if path.suffix == ".json":
            return json.load(f)
        else:
            # 排除空行
            return [line.strip() for line in f if line.strip()]
