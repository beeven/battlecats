
offset_nono = 6925
index_nono = 112

offset_start = offset_nono - index_nono * 4
offset_start = 6477

offset_active_end = 6476
index_active_end = 203
offset_active_start = offset_active_end - index_active_end * 4
print offset_active_start

offset_revolution_mr_m = 12897

def get_index_by_offset(offset):
    return (offset - offset_start)//4

def get_offset_by_index(index):
    return index * 4 + offset_start
