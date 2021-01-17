n, m, k = map(int, input().split(' '))
objects = list(map(int, input().split(' ')))
assert len(objects) == n, 'plz insert size of {} objects, inserted is {}'.format(n, len(objects))
j = 0
current_box_remain_space = k
remain_boxes = m
for o in reversed(objects):
    if o > k:
        break
    if remain_boxes == 1 and o > current_box_remain_space:
        break
    if o <= current_box_remain_space:
        current_box_remain_space -= o
    else:
        remain_boxes -= 1
        current_box_remain_space = k - o
    j = j + 1
print(j)
