# Create your views here.

from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from function import *
from bs4 import BeautifulSoup

def IndexHandler(request):
    return render_to_response('index.html')

def Bnuoj(cid):
    try:
        url = 'http://www.bnuoj.com/bnuoj/contest_info.php?cid=' + cid;
        data = fetch(url)
        soup = BeautifulSoup(data)
        contest = proto()
        contest.url = 'http://www.bnuoj.com/bnuoj/contest_show.php?cid=' + cid;
        contest.title = soup.find(attrs={'class' : 'pagetitle'}).text.strip()
        contest.source = soup.find(attrs={'class' : 'sidebar_item'}).p.text.strip()
        problem = []
        soup = soup.find(attrs={'id' : 'cplist'})
        soup = soup.find(name='tbody')
        for i in soup.find_all(name='tr'):
            s = i.find_all(name='td')
            a = proto()
            a.id = s[1].text
            a.url = contest.url + s[1].a['href']
            a.title = s[2].text.strip()
            problem.append(a)
        return render_to_response('contest.html', {'contest' : contest, 'problem' : problem})
    except:
        return HttpResponse('Invalid Contest')

def Hust(cid):
    try:
        url = 'http://acm.hust.edu.cn/vjudge/contest/view.action?cid=' + cid
        data = fetch(url)
        soup = BeautifulSoup(data)
        contest = proto()
        contest.url = url
        contest.title = soup.find(attrs={'id' : 'contest_title'}).text.strip()
        contest.source = soup.find(attrs={'class' : 'description'}).text.strip()
        problem = []
        soup = soup.find(name='table', attrs={'id' : 'viewContest'})
        soup = soup.find_all(name='tr')
        id = 0
        for i in soup[1:]:
            j = i.find_all('td')[4]
            t = proto()
            t.id = chr(ord('A') + id)
            id += 1
            t.title = j.text.strip()
            t.url = 'http://acm.hust.edu.cn/vjudge/' + j.a['href']
            problem.append(t)
        return render_to_response('contest.html', {'contest' : contest, 'problem' : problem})
    except:
        return HttpResponse('Invalid Contest')

@csrf_exempt
def AjaxHandler(request):
    oj = request.POST.get('oj')
    cid = request.POST.get('cid')
    if  oj == 'BNUOJ':
        return Bnuoj(cid)
    elif oj == 'HUST':
        return Hust(cid)
    else:
        return HttpResponse('Invalid OJ')