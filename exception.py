class TestException(Exception):
    ''' Test error raised '''
    def __str__(self):
        return '%s.%s: Test error raised' % (self.args[0], self.args[1])

# try:
#     raise TestException('Test error customed')
# except TestException, e:
#     print 'e.message: ', e.message, '; str(e)', str(e)


print dir(TestException), '\n============='
# raise TestException('TestError', 'Func')
raise NotImplementedError('EEEE', 'DDDD')
