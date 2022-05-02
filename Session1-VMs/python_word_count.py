file = open('romeo-juliet-prologue.rtf', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))