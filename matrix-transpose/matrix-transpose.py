import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    ans=[[0]*len(A) for i in range(len(A[0]))]
    # first value is no of rows * columns, R*C
    for i in range(len(A)):
        v=[]
        for j in range(len(A[0])):
            ans[j][i]=A[i][j]
    return np.array(ans)
            