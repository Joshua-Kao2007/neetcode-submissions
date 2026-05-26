class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # simply have a count of the students left, if there's a count left of the current thing on sandwiches then good, else false
        cntStudents = Counter(students)
        cnt = 0
        for sandwich in sandwiches:
            if cntStudents[sandwich] and cntStudents[sandwich] > 0:
                cntStudents[sandwich]-=1
            else:
                return sum(cntStudents.values())
        return 0