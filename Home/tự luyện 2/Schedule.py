with open('Schedule.inp', 'r') as f:
    T = int(f.readline())
    with open('Schedule.out', 'w') as output_file:
         for _ in range(T):
            N, X = map(int, f.readline().split())

            # Tính thời gian chờ của bệnh nhân cuối cùng
            last_patient_wait = X + 10 * (N - 1) - X * N
            if last_patient_wait<0:
                last_patient_wait=0
            
            # In ra thời gian chờ
            output_file.write(f'{last_patient_wait} \n')