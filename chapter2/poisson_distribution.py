from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# https://www.w3schools.com/python/numpy_random_poisson.asp

def random_poisson():
    # ポアソン分布とは、(どの時点でも同様な起こりやすさでランダムに起こる現象と仮定した場合に)「単位時間あたりに平均 λ 回起こる現象が、単位時間に k 回起きる確率」を表す
    # https://atarimae.biz/archives/7372#:~:text=%E3%83%9D%E3%82%A2%E3%82%BD%E3%83%B3%E5%88%86%E5%B8%83%E3%81%A8%E3%81%AF%E3%80%81(%E3%81%A9%E3%81%AE,%E3%82%8F%E3%82%8C%E3%82%8B%E7%A2%BA%E7%8E%87%E5%88%86%E5%B8%83%E3%81%AE%E3%81%93%E3%81%A8%E3%80%82
    # ポアソン分布に従う配列の生成
    x = random.poisson(lam=2, size=10)
    print(x)


def plot_poisson():
    sns.distplot(random.poisson(lam=2, size=1000), kde=False)
    plt.show()


if __name__ == '__main__':
    random_poisson()
    plot_poisson()
