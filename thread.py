import threading

thread_share = []


class Thread1(threading.Thread):
    def __init__(self, share, lock=None):
        threading.Thread.__init__(self)
        self.count = 0
        self.share = share
        self.lock = lock or threading.Lock()

    def run(self):
        while self.count < 20:
            # time.sleep(1)
            try:
                self.share.append(self.count)
                self.lock.acquire()
                print 'append success', self.count
                print 'the share appended', self.share
                self.lock.release()
                self.count = self.count + 1
            except:
                print 'append except !!! list lenght:', len(self.share)


class Thread2(threading.Thread):
    def __init__(self, share, lock=None):
        threading.Thread.__init__(self)
        self.share = share
        self.lock = lock or threading.Lock()

    def run(self):
        pop = 0
        print 'pop out running'

        while pop < 19:
            # time.sleep(1)
            try:
                if len(self.share):
                    pop = self.share.pop(0)
                    self.lock.acquire()
                    print 'pop out %d' % pop
                    print 'the share poped', self.share
                    self.lock.release()
            except:
                print 'pop out except'


if __name__ == '__main__':
    lock = threading.Lock()
    t1 = Thread1(thread_share)
    t2 = Thread2(thread_share)
    t2.start()
    t1.start()
