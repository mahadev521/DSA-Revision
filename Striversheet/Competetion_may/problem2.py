# similar to minimal distance between two identical numbers in an array
def minimumCardPickup(self, cards: List[int]) -> int:
    seen = {}
    minLen=float('inf')
    n=len(cards)
    for i in range(n):
        if cards[i] in seen:
            minLen = min(minLen, i-seen[cards[i]]+1)
        seen[cards[i]]=i
    if minLen>n : return -1
    return minLen