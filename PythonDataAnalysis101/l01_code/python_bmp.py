import struct

with open('sample.bmp', 'rb') as f:
    header = struct.unpack('<2c6I2H', f.read(30))
    print(header)
    print('图片大小：%d' % header[2])
    print('实际图像偏移量：%d' % header[4])
    print('header字节数：%d' % header[5])
    print('宽度：%d' % header[6])
    print('高度：%d' % header[7])
    print('颜色数：%d' % header[9])
    
