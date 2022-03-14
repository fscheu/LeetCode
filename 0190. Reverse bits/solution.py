class Solution(object):

    def reverseBits(self, n):
        bit_str = '{0:032b}'.format(n)
        reverse_str = bit_str[::-1]
        return int(reverse_str, 2)