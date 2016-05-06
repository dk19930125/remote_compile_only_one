#-*-coding:utf-8-*-
from django.test import TestCase

# Create your tests here.
import os
work_dir = os.path.dirname(os.path.realpath(__file__))+'/run_program/main.py'
with open(work_dir,"w") as f:
    f.write(u"我的".encode("utf8"))
