try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
s = search(query='site:*.ae',num=10,stop=100)
for j in s:
    print(j)