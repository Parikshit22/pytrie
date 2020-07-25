class Node:
    def __init__(self):
        self.children = [None]*26
        self.isend = False
        
class trie:
    def __init__(self,):
        self.__root = Node()
        
    def __len__(self,):
        return len(self.search_byprefix(''))
    
    def __str__(self):
        ll =  self.search_byprefix('')
        string = ''
        for i in ll:
            string+=i
            string+='\n'
        return string
        
    def chartoint(self,character):
        return ord(character)-ord('a')
    
    def remove(self,string):
        ptr = self.__root
        length = len(string)
        for idx in range(length):
            i = self.chartoint(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                raise ValueError("Keyword doesn't exist in trie")
        if ptr.isend is not True:
            raise ValueError("Keyword doesn't exist in trie")
        ptr.isend = False
        return
    
    def insert(self,string):
        ptr = self.__root
        length = len(string)
        for idx in range(length):
            i = self.chartoint(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                ptr.children[i] = Node()
                ptr = ptr.children[i]
        ptr.isend = True
        
    def search(self,string):
        ptr = self.__root
        length = len(string)
        for idx in range(length):
            i = self.chartoint(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                return False
        if ptr.isend is not True:
            return False
        return True
    
    def __getall(self,ptr,key,key_list):
        if ptr is None:
            key_list.append(key)
            return
        if ptr.isend==True:
            key_list.append(key)
        for i in range(26):
            if ptr.children[i]  is not None:
                self.__getall(ptr.children[i],key+chr(ord('a')+i),key_list)
        
    def search_byprefix(self,key):
        ptr = self.__root
        key_list = []
        length = len(key)
        for idx in range(length):
            i = self.chartoint(key[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                return None
        
        self.__getall(ptr,key,key_list)
        return key_list
        
