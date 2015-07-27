
offset_nono = 6925
index_nono = 112

offset_start = offset_nono - index_nono * 4
offset_start = 6477

offset_active_end = 6476
index_active_end = 203
offset_active_start = offset_active_end - index_active_end * 4
print offset_active_start

offset_revolution_rin = 0x173a5
index_revolution_rin = 18
offset_revolution_start = offset_revolution_rin - index_revolution_rin * 4



def get_level_index_by_offset(offset):
    return (offset - offset_start)//4

def get_level_offset_by_index(index):
    return index * 4 + offset_start

def get_revolution_index_by_offset(offset):
	return (offset - offset_revolution_start) // 4

def get_revolution_offset_by_index(index):
	return index * 4 + offset_revolution_start

__all__ = ['get_level_index_by_offset', 
	'get_revolution_offset_by_index', 
	'get_revolution_index_by_offset',
	'get_level_offset_by_index']