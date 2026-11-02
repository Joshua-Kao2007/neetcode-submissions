from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = 0
        student_cnt = Counter(students)
        while cnt < len(sandwiches):
            eat = sandwiches[cnt]
            if student_cnt.get(eat, 0) > 0:
                student_cnt[eat] -= 1
                cnt += 1
            else:
                return len(sandwiches) - cnt
        return len(sandwiches)-cnt