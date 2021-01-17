n, m, k = map(int, input().split(' '))
objects = list(map(int, input().split(' ')))
assert len(objects) == n, 'plz insert size of {} objects, inserted is {}'.format(n, len(objects))
j = 0
current_box_remain_space = k
remain_boxes = m
for o in reversed(objects):
        current_box_remain_space -= o
        if current_box_remain_space >= 0:
            j = j+1
        if current_box_remain_space < 0:
            remain_boxes -= 1
            if remain_boxes > 0:
                current_box_remain_space = k - o
                j = j + 1
            else:
                break
print(j)
