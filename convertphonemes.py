import phonemes

def words_to_phonemes(words):
	# Takes list of words and punctuation
	result = []
	for word in words:
		for letter in word:
			result.append(guess_phoneme(letter))
		result.append(phonemes.PAUSE_WORD)
	return result

def guess_phoneme(letter):
	l = letter.lower()
	if l == 'a':
		return phonemes.VOWEL_A
	elif l == 'b':
		return phonemes.CONS_B
	elif l == 'c':
		return phonemes.CONS_K
	elif l == 'd':
		return phonemes.CONS_D
	elif l == 'e':
		return phonemes.VOWEL_E
	elif l == 'f':
		return phonemes.CONS_F
	elif l == 'g':
		return phonemes.CONS_G
	elif l == 'h':
		return phonemes.CONS_H
	elif l == 'i':
		return phonemes.VOWEL_I
	elif l == 'j':
		return phonemes.CONS_J
	elif l == 'k':
		return phonemes.CONS_K
	elif l == 'l':
		return phonemes.CONS_L
	elif l == 'm':
		return phonemes.CONS_M
	elif l == 'n':
		return phonemes.CONS_N
	elif l == 'o':
		return phonemes.VOWEL_O
	elif l == 'p':
		return phonemes.CONS_P
	elif l == 'q':
		return phonemes.CONS_K # super primitive!
	elif l == 'r':
		return phonemes.CONS_R
	elif l == 's':
		return phonemes.CONS_S
	elif l == 't':
		return phonemes.CONS_T
	elif l == 'u':
		return phonemes.VOWEL_U
	elif l == 'v':
		return phonemes.CONS_V
	elif l == 'w':
		return phonemes.CONS_W
	elif l == 'x':
		return phonemes.CONS_Z
	elif l == 'y':
		return phonemes.CONS_Y
	elif l == 'z':
		return phonemes.CONS_Z
	elif l == '.':
		return phonemes.PUNC_PERIOD
	elif l == ',' or l == ';':
		return phonemes.PUNC_COMMA
	elif l == '!':
		return phonemes.PUNC_EXCLAIM
	elif l == '?':
		return phonemes.PUNC_QUESTION
	else:
		return phonemes.PAUSE_WORD