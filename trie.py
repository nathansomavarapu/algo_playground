from typing import List, Iterable
from collections import deque

import unittest

class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.end = False
    
    def __repr__(self):
        return self.children.__repr__()
    
    def __str__(self):
        return self.__repr__()

    def edges(self) -> Iterable:
        return self.children.items()

class Trie:

    def __init__(self, words: List[str]) -> None:
        
        self.root = self.construct_trie(words)

    def construct_trie(self, words: List[str]) -> TrieNode:

        root = TrieNode()
   
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end = True
        
        return root
    
    def search(self, word: str) -> bool:
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.end
    
    def all_words_with_prefix(self, prefix: str) -> List[str]:
        prefix_words = []

        prefix_list = list(prefix)

        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        
        if curr.end:
            prefix_words.append(prefix)
        
        st = deque([])
        for nc in curr.children:
            next_node = curr.children[nc]
            st.append(([nc], next_node))
                
        while len(st) != 0:
            curr_str, curr_node = st.pop()

            if curr_node.end:
                prefix_words.append(''.join(prefix_list + curr_str))
            
            for c, nei in curr_node.edges():
                new_str = curr_str[:]
                new_str.append(c)

                st.append((new_str, nei))

        return prefix_words
    
    def traversal(self) -> List[str]:
        all_words = []
        
        def traversal_helper(curr: 'TrieNode', curr_str = List[str]) -> None:
            if curr.end:
                all_words.append(''.join(curr_str))
            
            for (ch,nei) in curr.edges():
                traversal_helper(nei, curr_str + [ch])
        
        traversal_helper(self.root, [])
        return all_words


class TestTrie(unittest.TestCase):

    def test_construct(self):
        t = Trie(['hello', 'hell', 'help', 'yelp', 'tell'])
        
        self.assertTrue(t.search('hell'))
        self.assertTrue(t.search('yelp'))
        self.assertTrue(t.search('tell'))
        self.assertTrue(t.search('hello'))

        self.assertFalse(t.search('hellp'))
        self.assertFalse(t.search('yellp'))
        self.assertFalse(t.search('yellow'))
        self.assertFalse(t.search('yqlasd'))
    
    def test_prefix(self):
        t = Trie(['hello', 'hell', 'help', 'yelp', 'tell'])

        self.assertEqual(sorted(t.all_words_with_prefix('hel')), sorted(['help', 'hell', 'hello']))
        self.assertEqual(sorted(t.all_words_with_prefix('t')), sorted(['tell']))
        self.assertEqual(sorted(t.all_words_with_prefix('yel')), sorted(['yelp']))

        self.assertEqual(sorted(t.all_words_with_prefix('z')), sorted([]))

unittest.main()
            