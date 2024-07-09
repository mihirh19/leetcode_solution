class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avi = 0
        wait =0
        for a,t in customers:
            avi = max(avi,a) +t
            wait += avi -a
        
        return wait/len(customers)