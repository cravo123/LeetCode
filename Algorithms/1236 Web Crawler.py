# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

# Solution 1, typical DFS
class Solution:
    def dfs(self, url, parser, res):
        res.add(url)
        host = ".".join(url.split(".")[:2])
        
        for new_url in parser.getUrls(url):
            if new_url not in res and new_url.startswith(host):
                self.dfs(new_url, parser, res)
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = set()
        
        self.dfs(startUrl, htmlParser, res)
        
        res = list(res)
        
        return res

# Solution 2, BFS can be implemented in similar way
# t.b.c