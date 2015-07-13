__author__ = 'machin'


def check_command(pattern, command):
    bin_str = format(pattern, '0'+str(len(command))+'b')
    bin_command = ''.join(['1' if x.isalpha() else '0' for x in command])
    return bin_str == bin_command

print(check_command(42, "C2H5OH"))
