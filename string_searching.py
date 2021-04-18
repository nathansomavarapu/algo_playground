from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

class StringSearcher(ABC):

    @abstractmethod
    def search(self, needle: str, haystack: str) -> List[int]:
        """Find all matches of needle in haystack.

        :param needle: string to search for in haystack
        :type needle: str
        :param haystack: string to search in for needle
        :type haystack: str
        :return: List of locations where the needle string matches the haystack string
        :rtype: List[int]
        """
        raise NotImplementedError


class RabinKarpStringSearcher(StringSearcher):

    def __init__(self, a: int = 29, n: int = 10**9+9):
        """Initialize Rabin-Karp String Searcher.

        :param a: Base for polynomial hash, defaults to 29
        :type a: int, optional
        :param n: Modulus for polynomial hash, defaults to 10**9+9
        :type n: int, optional
        """
        self.a = a
        self.n = n
        
    
    def update_hash(self, hash: Optional[str], m: int, start_char: Optional[str], end_char: Optional[str]) -> str:
        """:param hash: Update the hash with a new start and end character or create
        the hash if the passed in hash is none, using the chars in start_char
        :type hash: Optional[str]
        :param m: Needle length for hash construction
        :type m: int
        :param start_char: Old starting character to remove
        :type start_char: Optional[str]
        :param end_char: New character to add
        :type end_char: Optional[str]
        :return: Return the updated hash
        :rtype: str
        """

        if not end_char and not hash:
            acc = 0
            for i, char in enumerate(start_char):
                int_char = ord(char) - ord('a')
                acc += (int_char * self.a**(m-i-1)) % self.n
            hash = acc
        else:
            hash -= ((ord(start_char) - ord('a')) * self.a**(m-1)) % self.n 
            hash *= self.a
            hash %= self.n
            hash += (ord(end_char) - ord('a')) % self.n
                
        return hash
    
    def search(self, needle: str, haystack: str) -> List[int]:
        m = len(needle)
        n = len(haystack)
        needle_hash = None
        hastack_hash = None
        matches = []

        needle_hash = self.update_hash(None, len(needle), needle, None)
        haystack_hash = self.update_hash(None, len(needle), haystack[:m], None)

        for j in range(n-m):
            if haystack_hash == needle_hash:
                matches.append(j)
            cs = haystack[j]
            ce = haystack[m+j]
            haystack_hash = self.update_hash(haystack_hash, len(needle), cs, ce)
        
        if haystack_hash == needle_hash:
            matches.append(j)
        
        return matches

if __name__ == '__main__':
    
    rkss = RabinKarpStringSearcher()

    n = 'reddit'
    h = 'getraickalskdrnasdlreddit'

    print(rkss.search(n,h))