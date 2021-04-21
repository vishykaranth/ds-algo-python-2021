class StringAlgorithms:
    # Function to find the first non-repeating character in
    # the string by doing only a single traversal of it
    def findNonRepeatingChar(self, chars, n):

        # dictionary to store character count and the index of its
        # last occurrence in the string
        dict = {}

        for index, char in enumerate(chars):
            frequency, prevIndex = dict.get(char, (0, index))
            dict[char] = (frequency + 1, index)

        # stores index of the first non-repeating character
        min_index = n

        # Traverse the dictionary and find a character with count 1 and
        # a minimum index of the string
        for key, values in dict.items():
            count, firstIndex = values
            if count == 1 and firstIndex < min_index:
                min_index = firstIndex

        return chars[min_index]