# 测试pythonlist
import matplotlib.pyplot as plt
import random
import time


log = print


axvline = plt.axvline


def test():
    ls = []
    data = [1, 2, 3]
    lines = [9, 'asd', 'line2']
    ls.append(data)
    ls.append(lines)

    secdata = ls[0]
    secline = ls[1]


    secdata.append('a, b, c')


    log('ls[0] = ({})'.format(ls[0]))
    log('len', len(secdata))
    log('index ', secdata.index(1))
    log('index ', secdata.index(2))
    log('index ', secdata.index(3))

    log('index ', secline.pop(1))

    log('after ', secline)


    # log('id of secdata', id(secdata), id(ls[0]))


    log('ls ({})'.format(ls))
    log('ls ({})'.format(ls[0]))
    # log('ls ({})'.format(ls[1]))
    # 同步增加
    # 同步删除
    # 同步修改
    pass


def ind_test():
    data = []
    line = []

    xs = random.sample(range(0, 10), 4)

    sectionlines =[data, line]
    secdata = sectionlines[0]
    secline = sectionlines[1]
    log('id of secdata', secdata is sectionlines)
    # 添加sectionline
    lastind = 1
    dataind = lastind
    # xdata = 1
    # secdata里面添加dataind
    # secline里面添加line
    if dataind not in secdata:
        log('没有添加过')
        secdata.append(dataind)
        secline.append(axvline(xs[dataind]))
        log('当前分区', sectionlines)
        log('曲线已添加  secline({})   secdata({}) sectionlines ({})'.format( secline, secdata, sectionlines))


    plt.show()

    for i in range(10):

        log(i)
        time.sleep(1)

    # 删除sectionline

    secdata = sectionlines[0]
    secline = sectionlines[1]
    log('id of secdata', secdata is sectionlines)
    # 添加sectionline
    dataind = lastind
    if dataind in secdata:
        ind = secdata.index(dataind)
        secdata.pop(ind)
        secline.pop(ind)
        log('曲线已移除  secline({})   secdata({}) sectionlines ({})', secline, secdata, sectionlines)
    plt.show()



def demo_random():
    # 1 - 100
    # random.seed(1)
    # x = prex * 100007 % xxxx
    # prex  = x 幂等性
    print(1, int(random.random() * 100))
    print(2, random.randint(0, 200))
    print(3, random.choice(range(0, 100, 10)))
    print(4, random.sample(range(0, 100), 4))
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print(5, a)


if __name__ == '__main__':
    # test()
    # demo_random()
    ind_test()
