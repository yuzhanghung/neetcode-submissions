class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = sorted(zip(timestamp, username, website))

        user_sites = defaultdict(list)
        for time, user, site in visits:
            user_sites[user].append(site)

        count = defaultdict(int)
        for user, site in user_sites.items():
            patterns = set(combinations(site, 3))
            for pattern in patterns:
                count[pattern] += 1

        best = max(count.values())
        return list(min(
            pattern for pattern in count
            if count[pattern] == best
        ))

        

