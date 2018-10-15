from __future__ import print_function

class A(object):
    def __init__(self,n):
        self._n = n

    @property
    def n(self):
        return "A:  "+ self._n


class B(object):
    def __init__(self,n):
        self._n = n

    @property
    def n(self):
        return "B:  "+ self._n

class M(object):
    use = B

    def __init__(self,n):
        self.myuse = M.use(n)

    @property
    def n(self):
        return self.myuse.n

if __name__ == '__main__':
    m = M('patata')
    print (m.n)
