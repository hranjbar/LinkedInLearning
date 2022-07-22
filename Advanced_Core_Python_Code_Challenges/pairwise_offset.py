def pairwise_offset(sequence, fillvalue="*", offset=0):
    ret = []
    j = 0
    for i in range(0, offset):
        if j < len(sequence):
            x = sequence[j], fillvalue
        else:
            x = fillvalue, fillvalue
        ret.append(x)
        j += 1
        
    for i in range(0, len(sequence)):
        if j < len(sequence):
            x = sequence[j], sequence[i]
        else:
            x = fillvalue, sequence[i]
        ret.append(x)
        j += 1

    return ret