class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #### Hashmap ####
        ans = []
        AllDomain = {}
        for address  in cpdomains:
            freq = int(address.split(" ")[0])
            domain = address.split(" ")[1]
            cache = domain.split(".")
            for i in range(len(cache)):
                form = cache[i:]
                domain = ".".join(form)
                if domain in AllDomain:
                    AllDomain[domain] += freq
                if domain not in AllDomain:
                    AllDomain[domain] = freq
        for k in AllDomain.keys():
            ans.append(str(AllDomain[k]) + " " + k)
        return ans