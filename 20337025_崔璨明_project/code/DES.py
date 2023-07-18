# -*- coding: utf-8 -*-
#IP置换表
IP_table=[58, 50, 42, 34, 26, 18, 10,  2,
  60, 52, 44, 36, 28, 20, 12,  4,
  62, 54, 46, 38, 30, 22, 14,  6,
  64, 56, 48, 40, 32, 24, 16,  8,
  57, 49, 41, 33, 25, 17,  9,  1,
  59, 51, 43, 35, 27, 19, 11,  3,
  61, 53, 45, 37, 29, 21, 13,  5,
  63, 55, 47, 39, 31, 23, 15,  7
]
#逆IP置换表
_IP_table=[40,  8, 48, 16, 56, 24, 64, 32,
  39,  7, 47, 15, 55, 23, 63, 31,
  38,  6, 46, 14, 54, 22, 62, 30,
  37,  5, 45, 13, 53, 21, 61, 29,
  36,  4, 44, 12, 52, 20, 60, 28,
  35,  3, 43, 11, 51, 19, 59, 27,
  34,  2, 42, 10, 50, 18, 58, 26,
  33,  1, 41,  9, 49, 17, 57, 25
]
#S1盒
S1=[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
    0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
    4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
    15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
]
#S2盒
S2=[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
    3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
    0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
    13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9
]
#S3盒
S3=[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
   13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
   13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
    1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12
]
#S4盒
S4=[7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
   13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
   10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
    3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
]
#S5盒
S5=[2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
   14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
    4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
   11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
]
#S6盒
S6=[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
    10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
     9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
     4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
]
#S7盒
S7=[4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
   13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
    1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
    6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
]
#S8盒
S8=[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
     1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
     7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
     2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
]
# S盒
S=[S1,S2,S3,S4,S5,S6,S7,S8]
#P盒
P_table=[16,  7, 20, 21,29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
        2,  8, 24, 14, 32, 27,  3,  9, 19, 13, 30,  6, 22, 11,  4, 25
]
#压缩置换表1，不考虑每字节的第8位，将64位密钥减至56位。然后进行一次密钥置换。
switch1_table=[ 57, 49, 41, 33, 25, 17,  9, 1, 58, 50, 42, 34, 26, 18,
               10,  2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
               63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
               14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4
]
#压缩置换表2，用于将循环左移和右移后的56bit密钥压缩为48bit
switch2_table=[14, 17, 11, 24,  1,  5, 3, 28, 15,  6, 21, 10,
              23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
              41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
              44, 49, 39, 56, 34, 53,46, 42, 50, 36, 29, 32
]
#用于对数据进行扩展置换，将32bit数据扩展为48bit
extend_table=[32,  1,  2,  3,  4,  5, 4,  5,  6,  7,  8,  9,
             8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32,1
]

# 将字符转换为对应的Unicode码
def char_to_unicode_ascii(intext, length):
    results = []
    for i in range(length):
        results.append(ord(intext[i]))
    return results

# Unicode转bit
def unicode_to_bit(intext, length):
    results = []
    for i in range(length * 16):
        results.append((intext[int(i / 16)] >> (i % 16)) & 1)  # 一次左移一bit
    return results

# ASCII码转bit
def byte_to_bit(inchar, length):
    results = []
    for i in range(length * 8):
        results.append((inchar[int(i / 8)] >> (i % 8)) & 1)  # 一次左移一bit
    return results

# bit转Unicode码
def bit_to_unicode(inbit, length):
    results = []
    tmp = 0
    for i in range(length):
        tmp = tmp | (inbit[i] << (i % 16))
        if i % 16 == 15:
            results.append(tmp)
            tmp = 0
    return results

# 将bit转为ascii 码
def bit_to_byte(inbit, length):
    results = []
    tmp = 0
    for i in range(length):
        tmp = tmp | (inbit[i] << (i % 8))
        if i % 8 == 7:
            results.append(tmp)
            tmp = 0
    return results

# 将unicode码转为字符（中文或英文）
def unicode_to_char(inbyte, length):
    results = ""
    for i in range(length):
        results = results + chr(inbyte[i])
    return results

# 生成每一轮的key
def build_keys(input_k):
    results = []
    ascii_key = char_to_unicode_ascii(input_k, len(input_k))
    init_key = byte_to_bit(ascii_key, len(ascii_key))
    KEY_0 = [0 for i in range(56)]
    KEY_1 = [0 for i in range(48)]
    # 进行密码压缩置换1，将64位压缩为56
    for i in range(56):
        KEY_0[i] = init_key[switch1_table[i] - 1]
    # 16轮的密码生成
    for i in range(16):
        # 左移的次数
        if (i == 0 or i == 1 or i == 8 or i == 15):     #压缩表左移1
            STEP = 1
        else:
            STEP = 2    #压缩表左移2
        #分两部分，每28bit一部分，循环左移
        for j in range(STEP):
            for k in range(8):
                tmp = KEY_0[k * 7]
                for m in range(7 * k, 7 * k + 6):
                    KEY_0[m] = KEY_0[m + 1]
                KEY_0[k * 7 + 6] = tmp
            tmp = KEY_0[0]
            for k in range(27):
                KEY_0[k] = KEY_0[k + 1]
            KEY_0[27] = tmp
            tmp = KEY_0[28]
            for k in range(28, 55):
                KEY_0[k] = KEY_0[k + 1]
            KEY_0[55] = tmp
        #56位压缩为48位
        for k in range(48):
            KEY_1[k] = KEY_0[switch2_table[k] - 1]
        results.extend(KEY_1)
    return results

def DES_Aglorithm(text, key, option):
    results = build_keys(key)
    final_text_bit = [0 for i in range(64)]
    final_text_unicode = [0 for i in range(4)]
    if option == 0:  # 为加密
        tmpText = [0 for i in range(64)]  # 将L部分和R部分合并成64位的结果
        extend_res = [0 for i in range(48)]  # R部分的扩展结果
        unicode_text = char_to_unicode_ascii(text, len(text))
        bit_text = unicode_to_bit(unicode_text, len(unicode_text))
        init_switch = [0 for i in range(64)]  
        # 初始IP置换
        for i in range(64):
            init_switch[i] = bit_text[IP_table[i] - 1]
        # 64位明文分为左右两部分
        L = [init_switch[i] for i in range(32)]
        R = [init_switch[i] for i in range(32, 64)]
        # 开始进行16轮运算
        for i in range(16):
            tmpR = R  # 用于临时盛放R
            # 将32位扩展为48位
            for j in range(48):
                extend_res[j] = R[extend_table[j] - 1]
            key_i = [results[j] for j in range(i * 48, i * 48 + 48)]
            # 与key值进行异或
            res_of_xor = [0 for j in range(48)]
            for j in range(48):
                if key_i[j] != extend_res[j]:
                    res_of_xor[j] = 1
            Sbox_result = [0 for k in range(32)]
            # S盒替换
            for k in range(8):
                row = res_of_xor[k * 6] * 2 + res_of_xor[k * 6 + 5]
                col = res_of_xor[k * 6 + 1] * 8 + res_of_xor[k * 6 + 2] * 4 + res_of_xor[k * 6 + 3] * 2 + res_of_xor[
                    k * 6 + 4]
                tmp = S[k][row * 16 + col]
                for m in range(4):
                    Sbox_result[k * 4 + m] = (tmp >> m) & 1
            Pbox_result = [0 for k in range(32)]
            # P盒置换
            for k in range(32):
                Pbox_result[k] = Sbox_result[P_table[k] - 1]
            # 与L部分的数据进行异或
            res_of_xor_l = [0 for k in range(32)]
            for k in range(32):
                if L[k] != Pbox_result[k]:
                    res_of_xor_l[k] = 1
            # 将临时保存的R部分值，即tmpR复制给L
            L = tmpR
            R = res_of_xor_l
        # 交换
        L, R = R, L
        # 合并
        tmpText = L
        tmpText.extend(R)
        # IP逆置换
        for k in range(64):
            final_text_bit[k] = tmpText[_IP_table[k] - 1]
        final_text_unicode = bit_to_byte(final_text_bit, len(final_text_bit))
        res_of_char = unicode_to_char(final_text_unicode, len(final_text_unicode))
        return res_of_char
    else: 
        tmpText = [0 for i in range(64)] 
        extend_res = [0 for i in range(48)]  
        unicode_text = char_to_unicode_ascii(text, len(text))
        bit_text = byte_to_bit(unicode_text, len(unicode_text))
        init_switch = [0 for i in range(64)] 
        # 初始IP置换
        for i in range(64):
            init_switch[i] = bit_text[IP_table[i] - 1]
        # 64位明文分为两部分
        L = [init_switch[i] for i in range(32)]
        R = [init_switch[i] for i in range(32, 64)]
        # 16轮的循环
        for i in range(15, -1, -1):
            tmpR = R 
            # 将32位扩展为48位
            for j in range(48):
                extend_res[j] = R[extend_table[j] - 1]
            key_i = [results[j] for j in range(i * 48, i * 48 + 48)]
            # 与key值异或
            res_of_xor = [0 for j in range(48)]
            for j in range(48):
                if key_i[j] != extend_res[j]:
                    res_of_xor[j] = 1
            Sbox_result = [0 for k in range(32)]
            # S盒替换
            for k in range(8):
                row = res_of_xor[k * 6] * 2 + res_of_xor[k * 6 + 5]
                col = res_of_xor[k * 6 + 1] * 8 + res_of_xor[k * 6 + 2] * 4 + res_of_xor[k * 6 + 3] * 2 + res_of_xor[
                    k * 6 + 4]
                tmp = S[k][row * 16 + col]
                for m in range(4):
                    Sbox_result[k * 4 + m] = (tmp >> m) & 1
            Pbox_result = [0 for k in range(32)]
            # P盒置换
            for k in range(32):
                Pbox_result[k] = Sbox_result[P_table[k] - 1]
            # 与L部分的数据进行异或
            res_of_xor_l = [0 for k in range(32)]
            for k in range(32):
                if L[k] != Pbox_result[k]:
                    res_of_xor_l[k] = 1
            # 将临时保存的R部分值，即tmpR复制给L
            L = tmpR
            R = res_of_xor_l
        # 交换
        L, R = R, L
        # 合并
        tmpText = L
        tmpText.extend(R)
        # IP逆置换
        for k in range(64):
            final_text_bit[k] = tmpText[_IP_table[k] - 1]
        final_text_unicode = bit_to_unicode(final_text_bit, len(final_text_bit))
        res_of_char = unicode_to_char(final_text_unicode, len(final_text_unicode))
        return res_of_char

if __name__=='__main__':
    while(True):
        option = input("########################################\nchoose:\n加密:0     解密:1\n")
        while(not(option=='0'or option=='1')):
            print("请输入0或1")
            option = input("choose:\n加密:0     解密:1\n")
        res = ""
        if option == '0':
            text = input("输入明文: ")
            print(" ".join(["明文:\n", text]))
            length = len(text)
            text = text + (length % 4) * " "
            length = len(text)
            key = input("输入8位密码: ")

            while (len(key) != 8):
                print("oops....")
                key = input("输入8位密码: ")

            print("密文：", end=" ")
            for i in range(int(length / 4)):
                tmpText = [text[j] for j in range(i * 4, i * 4 + 4)]
                res = "".join([res, DES_Aglorithm(tmpText, key, int(option))])
            print(res)
            file=open('cipertext.txt','w',encoding='utf-8')
            file.write(res)
            file.close()
        if option == '1':
            file=open('cipertext.txt','r',encoding='utf-8')
            text=file.read()
            length = len(text)
            key = input("输入8位密码: ")
            while (len(key) != 8):
                print("oops....")
                key = input("输入8位密码: ")
            print("解密结果：", end=" ")
            for i in range(int(length / 8)):
                tmpText = [text[j] for j in range(i * 8, i * 8 + 8)]
                res = "".join([res, DES_Aglorithm(tmpText, key, int(option))])
            print(res)
            file.close()
            break