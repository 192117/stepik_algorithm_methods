n = int(input())
parents = list(map(int, input().split()))

def height(array):
    max_tree = dict()
    max_h = 0
    for leaf in array:
        current_h = 1
        current_leaf = leaf
        while True:
            if current_leaf == -1:
                break
            current_leaf = array[current_leaf]
            if max_tree.get(current_leaf, None) is not None:
                current_h += max_tree[current_leaf]
                break
            current_h += 1
        if max_tree.get(leaf, None) is None:
            max_tree[leaf] = current_h
        if current_h > max_h:
            max_h = current_h
    return max_h

print(height(parents))


# def height(r):
#     h = 1
#     for i in range(len(parents)):
#         if parents[i] == r:
#             h = max(h, 1+height(i))
#     return h
#
#
# print(height(parents.index(-1)))
