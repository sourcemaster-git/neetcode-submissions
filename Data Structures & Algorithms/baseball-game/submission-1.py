class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for operation in operations:
            if operation.lstrip("-").isdigit():
                st.append(int(operation))
            elif operation == '+':
                n = len(st)
                x = st[n - 1] + st[n - 2]
                st.append(x)
            elif operation == 'D':
                x = st[-1] * 2
                st.append(x)
            elif operation == 'C':
                st.pop()
        return sum(st)