def int_to_gray(n):
    return n ^ (n >> 1)

def generate_gray_code(M):
    return [int_to_gray(i) for i in range(M)]
