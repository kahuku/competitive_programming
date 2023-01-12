from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains = defaultdict(int)
        for site in cpdomains:
            num, url = int(site.split()[0]), site.split()[1]
            subdomains[url] += num
            for i, char in enumerate(url):
                if char == '.':
                    part_url = url[i+1:]
                    subdomains[part_url] += num
        return [str(subdomains[key]) + " " + key for key in subdomains.keys()]