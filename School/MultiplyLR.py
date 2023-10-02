with open('MultiplyLR.inp','r') as f:

    T = int(f.readline())  # Số bộ dữ liệu cần kiểm tra
    results = []  # Danh sách kết quả
    for _ in range(T):
        N = int(f.readline())  # Số phần tử của dãy
        A = list(map(int, f.readline().split()))  # Các phần tử của dãy

        left_sum = sum(A[:N//2])  # Tính tổng các phần tử ở phần trái
        right_sum = sum(A[N//2:])  # Tính tổng các phần tử ở phần phải

        result = left_sum * right_sum  # Tính tích hai tổng
        results.append(result)
with open('MultiplyLR.out','w') as f:
    for result in results:
            f.write(str(f'{result}\n'))  # In kết quả