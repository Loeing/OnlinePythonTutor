import os


def parent():
    fpid = os.fork()
    count = 0
    if fpid < 0:
        print 'error'
    elif fpid == 0:
        print "This is the child process, my process id is " + str(os.getpid())
        count = count + 1
    else:
        print "This is the parent process, my process id is " + str(os.getpid())
        count = count + 1

parent()
