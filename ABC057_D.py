from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="057"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''4 2 2
2 3 3 3'''
y = '''
'''
additional_case = [x]
test_case += additional_case
print(test_case)

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,A,B=map(int,input().split())
  V=list(map(int,input().split()))
  V.sort(reverse=True)
  print(sum(V[:A])/A)
  if len(set(V[:A]))==1:
    n=V.count(V[0])
    ans=0
    for i in range(A,min(B,n)+1):
      tmp=1
      for j in range(i):
        tmp=tmp*(n-j)//(j+1)
      ans+=tmp
  else:
    n,m=V.count(V[A-1]),V[:A].count(V[A-1])
    ans=1
    for i in range(m):
      ans=ans*(n-i)//(i+1)
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])