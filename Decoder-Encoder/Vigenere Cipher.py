import sys


def de_vigenere_cipher(cipher_text, key, n):
    res = ""
    char_num = {chr(i): i - 65 for i in range(65, 91)}
    num_char = {i - 65: chr(i) for i in range(65, 91)}
    j = 0
    for c in cipher_text:
        if c == ' ':
            res += c
        else:
            k = key[j % len(key)]
            encode_num = (char_num[c] - char_num[k]) % n
            ltr = num_char[encode_num]
            res += ltr
            j += 1
    return res


def get_idxed_letters_freq(text, n, idx, key_len):
    freq = {chr(i): 0 for i in range(65, 91)}
    count = 0
    for i in range(len(text)):
        if i % key_len == idx:
            c = text[i]
            if c != " ":
                freq[c] += 1
                count += 1
    mean_val = 0
    for j in freq:
        freq[j] /= count
        mean_val += freq[j]
    return freq, mean_val / n

def get_letters_freq(text,n):
    freq = {chr(i):0 for i in range(65,91)}

    for i in text:
        if i!=" ":
            freq[i] += 1
    mean_val = 0
    for j in freq:
        freq[j]/=len(text)
        mean_val += freq[j]
    return freq, mean_val/n

def get_variance(letter_freq_dict, mean,n):
    temp=0
    for i in letter_freq_dict:
        temp += (letter_freq_dict[i]-mean)**2
    return temp/n

def get_shift_number(english_freq_dict, letter_freq_dict):
    ans_shift=0
    difference =26
    for shift in range(26):
        distance=0
        for num in range(65,91):
            num_after_shift = num+shift
            if num_after_shift>90:
                num_after_shift-=26
            ch1=chr(num)
            ch2=chr(num_after_shift)
            distance += (english_freq_dict[ch1]-letter_freq_dict[ch2])**2
        if distance<difference:
            difference=distance
            ans_shift= shift
    return ans_shift

def main():

    inFile = sys.argv[1]
    file = open(inFile, "r")
    text = file.read()
    cipher_text1 = text.upper()
    file.close()
    n=26
    ENGLISH_LETTER_FREQ ={
            'A': 0.08167, 'H': 0.06094, 'O': 0.07507, 'V': 0.00978,
            'B': 0.01492, 'I': 0.06996, 'P': 0.01929, 'W': 0.02360,
            'C': 0.02782, 'J': 0.00153, 'Q': 0.00095, 'X': 0.00150,
            'D': 0.04253, 'K': 0.00772, 'R': 0.05987, 'Y': 0.01974,
            'E': 0.12702, 'L': 0.04025, 'S': 0.06327, 'Z': 0.00074,
            'F': 0.02228, 'M': 0.02406, 'T': 0.09056,
            'G': 0.02015, 'N': 0.06749, 'U': 0.02758
        }
    mean_val =0
    for i in ENGLISH_LETTER_FREQ:
        mean_val += ENGLISH_LETTER_FREQ[i]
    MEAN_FREQ = mean_val/n
    english_variance =get_variance(ENGLISH_LETTER_FREQ,MEAN_FREQ,n)
    
    # method of mean variance to find length of keyword
    '''cipher_text1 = "ZSDWVCYGGEPYBODQVVHZRGICVLLNVHSTDWBGGMTNIAWCRGVEQDFVPYWHQREWLUGKSHXSLY" \
                   "LBRHHZRGSLSKWGKSOTHLSUWRWAMABCFHLZJDMXPYZBBQPPZSRGKTIORHVHEWLPVQHZUHAZ" \
                   "LZPVHZRGRTSUWGUWDTAWGKSMPPBUHKLHHVBORXPUXNVHQXMBLDBOWLPNGGPTUBUHZZGKTV" \
                   "QUDRVURDBOVVLRDRTHKMNGVPHHQQZSSPCMARPFHPVRVGHXAPGKSOTHLNUSEWLGQHOOGVGP" \
                   "HODZLLFRTEAFEUDHAGVWSKOGTDMJLZWHHEGKSXVHZRGGLXKQSKSDPFAGKSJPYMQHOOIOIG" \
                   "VDCDVNRQCFVONBUAPLPTYKOOZUWJQHSTFEBXZOSYITKWXXUBBWVPFBIEUSWHVWAHFZGSIG" \
                   "HFSTDQFKSOXAPNGPPTUTNWSCGHBUHFEWHVFRCYTYULPCEWLZGRZOBLBUDHOTHLZHBDXUOA" \
                   "RGZCNAUHDFIPVZBKPIUCEVSDPPLGKSDPTMGKWYVDQYOFZNJMEHDWXLLAHJPGIMYLSGTHVL" \
                   "WVTCNGBXVPPYIGDKZBHVFWWEIOMEHOCTAPVQUDIVJROSLGUMQHJPCMZBPHSTKMNGVTHCWV" \
                   "FSPROWRGHZDSWHGWYIOMGZWWXANBUSDIDMUDJPPSWAJFTSLJRICCTBATDFPSWWVQHPSVCG" \
                   "HWRWALNBGXPFJRQWYTHVQQWRWAQFIOWAPVTVSCLHGZDFCDFKRJZLCJMQDHEWLAXBKTIOLV" \
                   "VWYILZRVHTIKWRVHSPAMIHFJSHGNECFIAPVVHTBLIEHMZJBVZDBYTKJLWVPSHZXJOCTKEV" \
                   "OZNDBTQVSPIOMGLUSIUMFVOCDBVQJOCTKAZRIEWAPREOCTSGFXDAGLAFHRLCNMELBSXZML" \
                   "HGFCKMEWVPIOQPNPWPJSURCODMPVVQWDHSTDFPSOIQVDPCANBUHJNLIEVWYIOMALUSIZEN" \
                   "WQSBHVNQRMDFIAGVPLHAARHLRJCFWCXTKBBESTCNUNGSWXNPGRTJTAQGZODBVZRWVLCAPN" \
                   "WIYSLZGKSHDBVQHRAGPLRZWWAJWHORDTUARVCXTAPVQUPAZMVQHSTVTQHFXPUGBXQZJSLG" \
                   "DGETPBNQSCKVCFWSYHPWAWVLIJIZHDPGPTBXGNAVARWCQTHZJLZWHOIEHRSXZCAHODTOMU" \
                   "DRMTLVSRICNLIEVCYIOMJDZWIOMSLFDIAQZHVPWHLOHSYHLVGESJDULNOZEWLWYGGEDYQR"
'''
    initial_distance = english_variance**2
    for l in range(3, 22):
        var_list = []
        for idx in range(l):
            dict1, mean1 = get_idxed_letters_freq(cipher_text1, n, idx, l)
            var1 = get_variance(dict1, mean1, n)
            var_list.append(var1)
        mean_var = sum(var_list) / len(var_list)
        distance = (mean_var-english_variance)**2
        if(distance<initial_distance):
            key_length=l
            initial_distance=distance

    key_word=""
    for i in range(key_length):
        letter_freq_dict, letter_mean = get_idxed_letters_freq(cipher_text1,n,i,key_length)
        shift_num = get_shift_number(ENGLISH_LETTER_FREQ,letter_freq_dict)
        key_character = chr(shift_num+65)
        key_word += key_character

    original_text=de_vigenere_cipher(cipher_text1,key_word,n)
    print(key_word)
    print(original_text)


if __name__ == '__main__':
    main()
