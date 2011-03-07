
import os,sys

def p(options,buildout):
    # adding maps files

    src  = os.path.join(options['location'], 'sbin', 'nginx')
    dst  = os.path.join(options['location'], 'bin', 'nginx')
    ddst = os.path.join(options['location'], 'bin' )
    if os.path.exists(src):
        if os.path.exists(dst):
            os.unlink(dst)
        if not os.path.exists(ddst):
            os.makedirs(ddst)
        os.rename(src, dst)



