class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for i in range(len(operations)):
            if operations[i] == 'D':
                scores.append(int(scores[-1]) * 2)
            elif operations[i] == 'C':
                scores.pop()
            elif operations[i] == '+':
                scores.append(int(scores[-1]) + int(scores[-2]))
            else:
                scores.append(operations[i])

        sum = 0
        for j in scores:
            sum += int(j)

        return sum