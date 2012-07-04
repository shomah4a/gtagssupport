#-*- coding:utf-8 -*-

import sys
import optparse

__version__ = '0.1.0'


def make_parser():

    opt = optparse.Option

    options = [
        opt('--root', '-r', dest='root', default=''),
        ]

    return optparse.OptionParser(option_list=options)



def init(opts, args):
    
    from gtagssupport import model

    model.initialize(opts.root)



def mkcache(opts, args):

    init(opts, args)

    from gtagssupport import model

    with model.Session() as sess:

        ent = model.Entry(declname='1000',
                          lineno='100',
                          file='adasfsad',
                          line='aaaaa')
        sess.add(ent)



def lookup(opts, args):

    init(opts, args)


commands = dict(mkcache=mkcache,
                lookup=lookup)


def main(args=sys.argv[1:]):


    def print_err():
        
        print >> sys.stderr, 'invalid command.'
        print >> sys.stderr, 'commands:', ', '.join(commands.keys())
    

    if len(args) < 1:
        print_err()
        return

    cmd, args = args[0], args[1:]

    if cmd not in commands:
        print_err()
        return

    parser = make_parser()

    opts, args = parser.parse_args(args)

    commands[cmd](opts, args)

    


    
    

    

    
