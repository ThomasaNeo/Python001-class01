# 作业一
"""
容器序列：list 、tuple、collections.deque
扁平序列：str
可变：list 、 dict
不可变：tuple
"""


# 作业二
def mymap(func, *iterables):
    for t in zip(*iterables):
        yield func(*t)


def plus(a):
    return a + 1


def add(a, b):
    return a + b


print(list(mymap(plus, [1, 2, 3])))
print(list(mymap(add, [1, 2, 3], [1, 2, 3])))

# 作业三
import time


def timer(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}运行时间：{end_time - start_time}')

    return wrapper()


@timer
def test1(s):
    time.sleep(s)


test1(3)
