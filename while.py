def con():
    print 'continue'
    continue


def bre():
    print 'break'
    break


n = 0

while n < 30:
    if n == 15:
        con()
        n = n + 1
    else:
        bre()

print 'end while'
