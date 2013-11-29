class Lexicon(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
		
	def do():	
		stuff = raw_input('> ')
		words = stuff.split()
		
	def directions():
		first_word = ('direction', 'north')
		second_word = ('direction', 'south')
		third_word = ('direction', 'east')
		fourth_word = ('direction', 'west')
		fifth_word = ('direction', 'down')
		sixth_word = ('direction', 'up')
		seventh_word = ('direction', 'left')
		eighth_word = ('direction', 'right')
		nineth_word = ('direction', 'back')
		sentence = [first_word, second_word, third_word, fourth_word, fifth_word, sixth_word, seventh_word, eighth_word, nineth_word]
	
	def verbs():
		first_word = ('verbs', 'go')
		second_word = ('verbs', 'stop')
		third_word = ('verbs', 'kill')
		fourth_word = ('verbs', 'eat')
		sentence = [first_word, second_word, third_word, fourth_word]
	
	
	def stop_words():
		first_word = ('stop_words', 'the')
		second_word = ('stop_words', 'in')
		third_word = ('stop_words', 'of')
		fourth_word = ('stop_words', 'from')
		fifth_word = ('stop_words', 'at')
		sixth_word = ('stop_words', 'it')
		sentence = [first_word, second_word, third_word, fourth_word, fifth_word, sixth_word]
	
	def nouns():
		first_word = ('nouns', 'door')
		second_word = ('nouns', 'bear')
		third_word = ('nouns', 'princess')
		fourth_word = ('nouns', 'cabinet')
		sentence = [first_word, second_word, third_word, fourth_word]
	
	def numbers():
		first_number = ('numbers', '0')
		second_number = ('numbers', '1')
		third_number = ('numbers', '2')
		fourth_number = ('numbers', '3')
		fifth_number = ('numbers', '4')
		sixth_number = ('numbers', '5')
		seventh_number = ('numbers', '6')
		eighth_number = ('numbers', '7')
		nineth_number = ('numbers', '8')
		tenth_number = ('numbers', '9')
		sentence = [first_number, second_number, third_number, fourth_number, fifth_number, sixth_number, seventh_number, eighth_number, nineth_number, tenth_number]
	
	def convert_number(s):
		try:
			return int(s)
		except ValueError:
			return None