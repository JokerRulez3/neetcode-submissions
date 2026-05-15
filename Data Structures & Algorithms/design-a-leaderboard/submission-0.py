class Leaderboard:

    def __init__(self):
        self.scores = {} # {player_id: current_score}
        self.heap = [] # Min-heap of (score, player_id)
        

    def addScore(self, playerId: int, score: int) -> None:
        new_total = self.scores.get(playerId, 0) + score
        self.scores[playerId] = new_total

        heapq.heappush(self.heap, (new_total, playerId))
        

    def top(self, K: int) -> int:
        top_entries = heapq.nlargest(K, self.scores.items(), key=lambda x: x[1])
        
        # Update heap (min-heap of the top k)
        self.heap = [(score, p_id) for p_id, score in top_entries]
        heapq.heapify(self.heap)
        
        # Update running sum in O(k)
        return sum(score for p_id, score in top_entries)
        

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
