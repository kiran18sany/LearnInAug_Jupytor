'''
import json

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

def encodeFile(filename,newFilename):
    with open(filename) as f:
        data = encodeString(f.read())
    output=bytearray()
    for item in data:
        output.extend(bytes(item[0],'utf-8'))
        output.extend(item[1].to_bytes(1,'big'))
    with open(newFilename,'wb') as binary_file:
        binary_file.write(output)
def decodeFIle(filename):
    with open(filename,'rb') as f:
        data = f.read()
        bytePairs = [data[i:i+2] for i in range(0,len(data),2)]
        encodedList = []
        for bytePair in bytePairs:
            encodedList.append((bytePair[:1].decode('utf-8'),int.from_bytes(bytePair[1:],'big')))
        return decodeString(encodedList)
        '''


import sys
import os
def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count += 1
    encodedList.append((prevChar, count))
    return encodedList


def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr += item[0] * item[1]
    return decodedStr


def encodeFile(filename, newFilename):
    with open(filename, "r", encoding="utf-8") as f:
        data = encodeString(f.read())
    output = bytearray()
    for item in data:
        output.extend(bytes(item[0], 'utf-8'))
        output.extend(item[1].to_bytes(2, 'big'))  # use 2 bytes for bigger runs
    with open(newFilename, 'wb') as binary_file:
        binary_file.write(output)


def decodeFile(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        bytePairs = [data[i:i+3] for i in range(0, len(data), 3)]  # 1 byte char + 2 byte count
        encodedList = []
        for bytePair in bytePairs:
            encodedList.append((bytePair[:1].decode('utf-8'),
                                int.from_bytes(bytePair[1:], 'big')))
        return decodeString(encodedList)


if __name__ == "__main__":
    # Example usage
    #encodeFile(r'C:\J_KIRAN\SampleFile.txt', "encoded.bin")
    encodeFile('SampleFile.txt', "encoded.bin")
    print("Encoding complete! File saved as encoded.bin")

    decoded_text = decodeFile("encoded.bin")
    #print("Decoded content:", decoded_text)

    print(f'Original file size: {os.path.getsize("SampleFile.txt")}')

    print(f'New file size: {os.path.getsize("encoded.bin")}')