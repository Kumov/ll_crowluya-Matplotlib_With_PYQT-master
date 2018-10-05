import sys
import os

from models import load
from models import save
from utils import log

# 1.指定目录加载文件
# 2.指定目录保存文件


# 加载文件
def get_current_path():
    # 获取当前文件目录
    paths = sys.path
    current_file = os.path.basename(__file__)
    for path in paths:
        try:
            if current_file in os.listdir(path):
                current_path = path
                break
        except (FileExistsError, FileNotFoundError) as e:
            print(e)


def test_path():
    path = os.getcwd()

    log(())

    pass


def test_load():
    test_path()
    # path =
    pass


def test():
    test_load()


if __name__ == '__main__':
    test()
    pass
