import math
import sys


def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print("Error opening or reading input file: ", filename)
        sys.exit()


def get_word_list(line_list):
    word_list = []
    for line in line_list:
        words_in_line = get_words_line(line)
        word_list = word_list + words_in_line
    return word_list


def get_words_line(line):
    word_list = []
    char_list = []
    for c in line:
        if c.isalnum():
            char_list.append(c)
        elif len(char_list) > 0:
            word = "".join(char_list)
            word = word.lower();
            word_list.append(word)
    if len(char_list) > 0:
        word = "".join(char_list)
        word = word.lower();
        word_list.append(word)
    return word_list


def count_frequency(word_list):
    L = []

    for word in word_list:
        for entry in L:
            if word == entry[0]:
                entry[1] += 1
                break
        else:
            L.append([word, 1])
    return L


def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[j] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_word_list(line_list)
    freq_mapping = count_frequency(word_list)
    insertion_sort(freq_mapping)

    print("File", filename, ":"),
    print(len(line_list), "lines,", )
    print(len(word_list), "words,", )
    print(len(freq_mapping), "distinct words")

    return freq_mapping


def inner_product(L1, L2):
    sum = 0.0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum+=count1*count2
    return sum


def vector_angle(L1, L2):
    numerator = inner_product(L1, L2)
    denumerator = math.sqrt(inner_product(L1, L1)*inner_product(L2,L2))
    return math.acos(numerator / denumerator)


def main():
    #if len(sys.argv) != 3:
     #if False:
        print("Usage: docdist1.py filename_1 filename_2")
    #else:
        # filename_1 = sys.argv[1]
        # filename_2 = sys.argv[2]
        filename_1 = '1.txt'
        filename_2 = '2.txt'
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
        print("The distance between the documents is: %0.6f (radians)" % distance)


if __name__ == "__main__":
    import profile

    profile.run("main()")
