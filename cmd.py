#!/usr/bin/env python
# coding: utf-8

import argparse


class Grouped(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        group, dest = self.dest.split('.', 2)
        groupspace = getattr(namespace, group, argparse.Namespace())
        setattr(groupspace, dest, values)
        setattr(namespace, group, groupspace)

parser = argparse.ArgumentParser(description='Test POCs All or with POC IDs.')
parser.add_argument('-p', '--poc',
                    dest='poc_ids', metavar='ID', nargs='+',
                    help='the POC IDs those want to run')

parser.add_argument("--sub1", action=Grouped,
                    dest='sub.sub1', default=argparse.SUPPRESS)
parser.add_argument("--sub2", action=Grouped,
                    dest='sub.sub2', default=argparse.SUPPRESS)

args = parser.parse_args()

if __name__ == '__main__':
    print '/n', args, '------------'
