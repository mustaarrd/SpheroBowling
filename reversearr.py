import numpy as np
import os
arr = np.array([[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 1, 1, 2, 2, 2, 2, 1]],
[[1, 1, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 1, 2, 2, 2, 2, 2, 2]],
[[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 1, 1, 2, 2, 2, 2, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 3, 1],
[1, 1, 2, 2, 2, 3, 1, 1],
[1, 1, 2, 2, 2, 3, 1, 1],
[1, 1, 1, 2, 2, 2, 3, 1],
[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 1, 1, 2, 2, 2, 2, 1]],
[[1, 1, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 1, 2, 2, 2, 2, 2, 2]],
[[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 1, 2, 2, 2, 2, 2, 2],
[1, 1, 1, 2, 2, 2, 2, 1]],
[[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 2, 2, 1, 1]],
[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 2, 2, 2, 3, 1],
[1, 1, 2, 2, 2, 3, 1, 1],
[1, 1, 2, 2, 2, 3, 1, 1],
[1, 1, 1, 2, 2, 2, 3, 1],
[1, 1, 1, 1, 2, 2, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]]])

#f = arr.reshape(-1, arr.shape[2])
f = np.array([np.rot90(slice_, k=-3) for slice_ in arr])


for i, slice_ in enumerate(f):
    filename = f'./slice_{i}.txt'
    np.savetxt(filename, slice_, fmt='%d')

    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        file.write('[')
        for line in lines:
            file.write('[' + ', '.join(line.strip().split()) + '],\n')
        file.write(']')

combined_filename = './combined_slices.txt'
with open(combined_filename, 'w') as combined_file:
    for i in range(len(f)):
        slice_filename = f'./slice_{i}.txt'
        with open(slice_filename, 'r') as slice_file:
            # 각 슬라이스 파일의 내용을 읽어서 합친 파일에 쓰기
            combined_file.write(slice_file.read())
            combined_file.write('\n\n')  # 슬라이스 간 구분을 위한 빈 줄 추가

# 필요없는 개별 슬라이스 파일 삭제 (선택 사항)
for i in range(len(f)):
    os.remove(f'./slice_{i}.txt')



