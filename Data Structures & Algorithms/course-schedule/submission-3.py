
class Course:

    def __init__(self):
        self.pre = {}
        self.children = {}


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = {}

        for course in prerequisites:
            if str(course[0]) not in courses:
                courses[str(course[0])] = Course()
            if str(course[1]) not in courses:
                courses[str(course[1])] = Course()
            courses[str(course[0])].pre = courses[str(course[0])].pre | courses[str(course[1])].pre
            courses[str(course[0])].pre[str(course[1])] = courses[str(course[1])]
            courses[str(course[1])].children = courses[str(course[1])].children | courses[str(course[0])].children
            courses[str(course[1])].children[str(course[0])] = courses[str(course[0])]
            for child in courses[str(course[0])].children:
                courses[child].pre |= courses[str(course[0])].pre
            if str(course[0]) in courses[str(course[1])].pre or str(course[1]) in courses[str(course[0])].children:
                return False
        
        return True


        