#Given a dictionary (list) of "words", find the longest chain possible
#where: you can remove any letter from the word and still be in the dictionary.

#match an input string with a given list
dict = {"nyc", "datascience", "python", "coding", "sqlanddatabase", "academy"}
str = "nycdatascienceacademyisaplacefordatasicne"

def find_word_chain(dict, str):
    matched_word = {}
    for word in dict:
        str_len = len(str)
        word_len = len(word)

        str_index = 0
        word_index = 0
        #find how many matches are there for each word
        while (str_index < str_len and word_index < word_len):
            if word[word_index] == str[str_index]:
                word_index += 1
            str_index += 1
        matched_word.update({word_index:word})
    #transform matching words with matched length into dataframe
    #redo here
    output = matched_word.get(max(matched_word.keys()))
    return(output)






#match each word from the list
dict = {"nyc", "datascience", "python", "coding", "sqlanddatabase", "academy",'abvaseudondaj','datainfomanagement'}

def find_word_chain(dict):
    result = {} #maxium length from each match
    for str in dict:
        matched_word = {} #matched length for each word
        for word in [x for x in dict if x not in str]:
            str_len = len(str)
            word_len = len(word)

            str_index = 0
            word_index = 0
            #find how many matches are there for each word
            while (str_index < str_len and word_index < word_len):
                if word[word_index] == str[str_index]:
                    word_index += 1
                str_index += 1
            matched_word.update({word_index:word})
        #transform matching words with matched length into dataframe
        result.update({max(matched_word.keys()):[str,matched_word.get(max(matched_word.keys()))]})
    print(result)
    result_values = result.get(max(result.keys()))[0] #return the word with the longest chain
    return(result_values)

chain_list = find_word_chain(dict)

chain_list


###offical answer:
def longest(word, word_set, cache):
    if word not in cache:
        now = 1
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in word_set:
                current = longest(new_word, word_set, cache)
                now = max(now, 1 + current)
        cache[word] = now
        return cache[word]
    else:
        return cache[word]

def longestChain(words):
    cache = {}
    word_set = set(words)
    current_max = 0
    for word in words:
        current_max = max(current_max, longest(word, word_set, cache))

    return current_max

longestChain(['asoidhoiqyewoiuq','asoidhoi','qw','word','words'])




def friendCircles(friends):
	n = len(friends)
	res = 0
	visited = [False] * n

	def dfs(i):
		visited[i] = True
		for j in range(n):
			if visited[j] or friends[i][j] != 'Y' or i == j: continue
			dfs(j)

	for i in range(n):
		if visited[i]:
			continue
		res += 1
		dfs(i)

	return res


def stringChains(words):
	if not words:
		return 0

	max_len = 0
	words.sort(key=lambda w: len(w))
	seq_len = {}
	for w in words:
		seq_len[w] = 1
		for i in range(len(w)):
			reduced = w[:i] + w[i + 1:]
			if reduced in seq_len and seq_len[reduced] + 1 > seq_len[w]:
				seq_len[w] = seq_len[reduced] + 1
		max_len = max(max_len, seq_len[w])
	return max_len
