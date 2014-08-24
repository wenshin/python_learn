# coding: utf-8

class AA(object):
    aa = 1


class A(object):
    class Meta(AA):
        pass

    @classmethod
    def _init(cls):
        cls.Meta.aa = 10

    def init(self):
        self.__class__._init()
        return self.__class__.Meta()


class ASon(A):
    pass

if __name__ == '__main__':
    a = A()
    b = a.init()
    print b.aa
    ason = ASon()
    print dir(ason)
