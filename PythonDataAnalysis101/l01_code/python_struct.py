import struct

# pack与unpack
# '>'代表big-endian编码
# 'I'代表4个字节的整数
# 'H'代表2字节无符号整数
print(struct.pack('>I', 1050624))
print(struct.pack('>I', 10240064))
print(struct.unpack('>IH', b'\x00\x9c\x40\x40\x7c\x80'))
