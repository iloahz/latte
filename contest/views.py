# Create your views here.

from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from function import *
from bs4 import BeautifulSoup

def IndexHandler(request):
    return render_to_response('index.html')

@csrf_exempt
def AjaxHandler(request):
    cid = request.POST.get('cid')
    url = 'http://www.bnuoj.com/bnuoj/contest_info.php?cid=' + cid;
    data = fetch(url)
    soup = BeautifulSoup(data)
    contest = proto()
    contest.url = 'http://www.bnuoj.com/bnuoj/contest_show.php?cid=' + cid;
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