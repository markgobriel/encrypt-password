def encrypt_password(msg, key):
    """
    Precondition:
        - len(msg) > len(key).
        - key is a string with distinct letters.
    """

    num_cols = len(key)
    num_rows = len(msg) // num_cols + 1
    curr_lst = []
    final_lst = []
    encrypted = ''

    x = len(msg) % len(key)
    full_row = (len(msg) - x) // len(key)

    while len(final_lst) != full_row:
        for i in range(len(msg) - (len(msg) % num_cols)):
            curr_lst.append(msg[i])
            if len(curr_lst) % num_cols == 0:
                final_lst.append(curr_lst)
                curr_lst = []

    while len(final_lst) != num_rows:
        for i in range(-x, 0):
            curr_lst.append(msg[i])
        for j in range(num_cols - (len(msg) % len(key))):
            curr_lst.append('.')
        final_lst.append(curr_lst)

    sort_by_col = []
    final_order = []
    for i in range(num_cols):
        for lst in final_lst:
            sort_by_col.append(lst[i])
        final_order.append(sort_by_col)
        sort_by_col = []

    sorted_char = []
    unsorted_char = []
    for char in key:
        sorted_char.append(char)
        unsorted_char.append(char)

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(sorted_char) - 1):
            if sorted_char[i] > sorted_char[i + 1]:
                sorted_char[i], sorted_char[i + 1] = sorted_char[i + 1], sorted_char[i]
                is_sorted = False

    char_index = []
    for char in sorted_char:
        char_index.append(unsorted_char.index(char))

    the_lst = []
    for index in char_index:
        the_lst.extend(final_order[index])

    encrypted = ''
    for char in the_lst:
        encrypted += char

    return encrypted.replace('.', '')
