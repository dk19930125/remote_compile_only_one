#-*-coding:utf-8-*-
import urllib
import chardet
from django.shortcuts import render

from django.http import HttpResponse
# from models import CompileInfo
import subprocess,os
from django.utils.http import urlquote
# Create your views here.
work_dir = os.path.dirname(os.path.realpath(__file__))+'/run_program/'
def homepage(request):
    return render(request,'first.html')
def index(request):
    result = request.GET["lang"]
    try:
        res = urllib.unquote(result)
    except Exception,e:
        print "e",e


    real_path = os.path.normpath('{0}main.py'.format(work_dir))
    # print real_path
    with open(real_path,'w') as f:
        f.write(res.encode("utf8"))

    res = subprocess.Popen('python {0}main.py'.format(work_dir),
       stdout = subprocess.PIPE,
       stderr = subprocess.PIPE,
       shell = True,
)
    out,err = res.communicate()
    if res.returncode == 0:
        # print "out",out
        return HttpResponse(out)
        # return render(request,'first.html',{'string':out})
    else:
        # print 'err',err
        # return HttpResponse(err)
        # err = urlquote(err
        return HttpResponse(err)
        # return render(request,'first.html',{'string':out})

def test(request):
    print "test is requests"
    return HttpResponse("123456")
# def

