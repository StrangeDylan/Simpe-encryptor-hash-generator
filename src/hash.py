def gethash(data : bytes):
    while len(data) % 16 != 0:
        for i in range(len(data)):
            data += (((data[i] ** 2 + 1) + data[i]) % 255).to_bytes(1, 'big')

    result = ''
    buffer = []
    dataLength = len(data)
    staticOffset = int(dataLength/16)
    currentOffset = 0

    while currentOffset != dataLength:
        buff = 0
        for i in range(staticOffset):
            buff += data[currentOffset + i]
        currentOffset += staticOffset
        buffer.append(buff)
    for i in range(16):
        for x in range(16):
            buffer[i] ^= buffer[x] + 16
        piece = hex(buffer[i] % 255)
        if len(piece) != 4:
            piece = '0' + piece[2]
        else:
            piece = piece[2:4]
        result += piece
    return 'dh' + result
