class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #If top of each queue matches, pop from front
        #If they done, move pop the top student, and add it to end
        #Return if the sandwich queue, and students queue has no possible solutions

        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                break
        
        return res


        