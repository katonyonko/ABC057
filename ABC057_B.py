from asyncio import AbstractEventLoop
from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="057"
#問題
problem="b"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,M=map(int,input().split())
  p=[list(map(int,input().split())) for _ in range(N)]
  c=[list(map(int,input().split())) for _ in range(M)]
  for i in range(N):
    tmp=10**10
    x,y=p[i]
    for j in range(M):
      xx,yy=c[j]
      if abs(x-xx)+abs(y-yy)<tmp:
        tmp=abs(x-xx)+abs(y-yy)
        ans=j+1
    print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])