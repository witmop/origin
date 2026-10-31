class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for t in range(k):
            index_max=gifts.index(max(gifts))
            maxi=max(gifts)
            maxi=int(sqrt(maxi))
            gifts[index_max]=maxi
        return sum(gifts)
