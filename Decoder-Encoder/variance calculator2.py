
def get_letters_freq(text,n):
    freq = {chr(i):0 for i in range(97,123)}

    for i in text:
        if i!=" ":
            freq[i] += 1
    mean_val = 0
    for j in freq:
        freq[j]/=len(text)
        mean_val += freq[j]
    return freq, mean_val/n

def get_idxed_letters_freq(text,n,idx,key_len):
    freq = {chr(i): 0 for i in range(97, 123)}
    count=0
    for i in range(len(text)):
        if i%key_len==idx:
            c = text[i]
            if c != " ":
                freq[c] += 1
                count +=1
    mean_val = 0
    for j in freq:
        freq[j] /= count
        mean_val += freq[j]
    return freq, mean_val / n

def get_variance(letter_freq_dict, mean,n):
    temp=0
    for i in letter_freq_dict:
        temp += (letter_freq_dict[i]-mean)**2
    return temp/n

def vinegere_cipher(plain_text,key, n):
    res=""
    char_num = {chr(i): i-97 for i in range(97, 123)}
    num_char = {i-97: chr(i) for i in range(97, 123)}
    j=0
    for c in plain_text:
        if c == ' ':
            res += c
        else:
            k = key[j%len(key)]
            encode_num=(char_num[c]+char_num[k])%n
            ltr = num_char[encode_num]
            res += ltr
            j+=1
    return res


def main():
    # Code block for Q2 (a)
    n = 26
    '''ENGLISH_LETTER_FREQ ={
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
    print(get_variance(ENGLISH_LETTER_FREQ,MEAN_FREQ,n))'''

    # Code block for Q2 (b)
    plain_text1 = "couragedthemtodothesamesomeoftheseconversationsoccurinpubliclyaccessed" \
                  "socialnetworkingsitesbutotherstakeplaceviaprivatemessagingplatformsthe" \
                  "seencrypteddirectmessagingplatformsaretremendouslyproblematicwhenusedb" \
                  "yterroristplottersinaworldwhereusershavesolecontroloveraccesstotheirde" \
                  "vicesandcommunicationsandsocaneasilyblockalllawfullyauthorizedaccessto" \
                  "theirdatathejurywouldnothavebeenabletoconsiderthatevidenceunlessthetru" \
                  "ckdriveragainsthisowninterestprovidedthedataandthetheoreticalavailabil" \
                  "ityofothertypesofevidenceirrelevanttothecasewouldhavemadenodifferencei" \
                  "nthatworldthegrimlikelihoodthathewouldgofreeisacostthatwemustforthrigh" \
                  "tlyacknowledgeandconsiderweareseeingmoreandmorecaseswherewebelievesign" \
                  "ificantevidenceresidesonaphoneatabletoralaptopevidencethatmaybethediff" \
                  "erencebetweenanoffenderbeingconvictedoracquittedifwecannotaccessthisev" \
                  "idenceitwillhaveongoingsignificantimpactsonourabilitytoidentifystopand"

    plain_dict, plain_mean = get_letters_freq(plain_text1,n)

    #Code block for Q2 (c)
    '''
    keys=["yz","xyz","wxyz","vwxyz","uvwxyz"]
    for key in keys:
        cipher_text = vinegere_cipher(plain_text1,key,n)
        print("cipher_text encrypted by key "+key+" is: \n",cipher_text)
        cipher_dict, cipher_mean = get_letters_freq(cipher_text,n)
        cipher_var = get_variance(cipher_dict,cipher_mean,n)
        print("variance of ciphertext encrypted by key "+key+" is ",cipher_var)
    '''

    # Code block for Q2 (d)
    keys = ["yz", "xyz", "wxyz", "vwxyz", "uvwxyz"]
    for key in keys:
        cipher_text = vinegere_cipher(plain_text1,key,n)
        var_list=[]
        for idx in range(len(key)):
            dict1, mean1 = get_idxed_letters_freq(cipher_text, n, idx, len(key))
            var1 = get_variance(dict1, mean1, n)
            var_list.append(var1)
        mean_var = sum(var_list)/len(var_list)
        print("mean variance of ciphertext encrypted by key "+key+" is ",mean_var)

    # Code block for Q2 (e)
    key_e = "uvwxyz"
    cipher_text_e = vinegere_cipher(plain_text1,key_e,n)
    for l in [2,3,4,5,6,7,8,9,10,11,12]:
        var_list = []
        for idx in range(l):
            dict1, mean1 = get_idxed_letters_freq(cipher_text_e, n, idx, l)
            var1 = get_variance(dict1, mean1, n)
            var_list.append(var1)
        mean_var = sum(var_list) / len(var_list)

if __name__ == '__main__':
    main()
