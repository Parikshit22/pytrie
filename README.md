# pytrie
Trie Data Structure can be used to store data in O(L) where L is the length of the string so for inserting N strings time complexity would be O(NL) the string can be searched in O(L) only same goes for deletion.
```
from pytrie import trie
t = trie()
t.insert("shubham")
t.insert("shubhi")
t.insert("minhaj")
t.insert("parikshit")
t.insert("pari")
t.insert("shubh")
t.insert("minakshi")
```
```
print(t.search("minhaj"))
print(t.search("shubhk"))
print(t.search_byprefix('m'))
print(len(t))
print(t.remove("minhaj"))
print(t)
```

### Code Oputpt ###
True
<br/>
False
<br/>
['minakshi', 'minhaj']
<br/>
7
<br/>
minakshi
<br/>
minhajsir
<br/>
pari
<br/>
parikshit
<br/>
shubh
<br/>
shubham
<br/>
shubhi



