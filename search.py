from googlesearch import search

# Search string 

query = "python"

for i in search(query, tld="com", num=10, stop=10, pause=2):

    print(i)