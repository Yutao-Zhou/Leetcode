class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #### simulation take and check ####
        # counter = 0
        # students = deque(students)
        # sandwiches = deque(sandwiches)
        # while counter < len(students) and students and sandwiches:
        #     student = students.popleft()
        #     sandwiche = sandwiches.popleft()
        #     if student != sandwiche:
        #         students.append(student)
        #         sandwiches.appendleft(sandwiche)
        #         counter += 1
        #     else:
        #         counter = 0
        # return len(students)
        
        #### simulation only look at it ####
        counter = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        while counter < len(students) and students and sandwiches:
            student = students.popleft()
            if student != sandwiches[0]:
                students.append(student)
                counter += 1
            else:
                sandwiches.popleft()
                counter = 0
        return len(students)