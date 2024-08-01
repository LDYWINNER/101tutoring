# 10.1
from PythonLabs.ElizaLab import *

Eliza.load(path_to_data('doctor.txt'))
#Eliza.run()

#Eliza.info()

# 10.2
# string search
s1 = 'I was afraid of the cow'
# find : a string method
# s.find(w) form (return -1 if w not in s)
# (return starting location of the w if w in s)
print(s1.find('cow'))
print(s1.find('horse'))

# Error
s2 = 'My cat is scowling at me'
print(s2.find('cow'))

# re : advanced form of string searching implemented in a Python library
# acronym for regular expression
# Regular expression : a pattern
# When we do a regular expression search, we are asking Python to find places in the string that match the pattern
# We can define simple patterns that require an exact match with a particular word like 'cow'
# We can also define more complicated patterns like 'any substring that starts with a 'c' and is at least 5 letters long'.

# Patterns : the ElizaLab objects we will use in our experiments
p = Pattern('cow')
p.add_response('Tell me more about your farm')
p.add_response('Go on')

p3 = Pattern('duck', ['I love ducks', 'How cute'])

# Regular expression : a type of string used in pattern matching operations
# Python has an extensive library of functions for defining regular expressions
# and using them in string processing applications

# How one might find all the numbers in the middle of the string
s = 'The farm had 31 cows and 2 ducks'
a = re.findall(r'\d+', s)
print(a)

# apply : a method used to see if an input sentence matches the pattern
# p.apply(s) form, p : a pattern object, s : sentence
b = p.apply('I milked the cow')
print(b)
x = p.apply('That cow was scary')
print(x)
# Response cycling one after another

print(p.apply('There were pigs, too'))

print(p.apply("The cat was scowling at me"))

p = Pattern("cow|pig|horse", ["Really?", "Go on"] )
# group : a set of words separated by vertical bars
print(p.apply("The cow slept in the barn"))
print(p.apply("The horse jumped the fence"))

p = Pattern("cow", ["Tell me more about your farm."] )
print(p.apply("I milked the cow"))
print(p.apply("That cow sleeps standing up"))
p.add_response("What made you think of cows just now?")
p.add_response("Do cows worry you?")
print(p.apply("The cow slept in the barn"))
print(p.apply("She had a cow"))
print(p.apply("No, not a real cow, she had a fit"))
print(p.apply("Do you know what a cow is?"))
print(p.apply("how now, Brown Cow"))
print(p.apply("those cows produce milk"))
print()
p2 = Pattern("Ruby|Perl|Python", ["The programming language?"])
print(p2.apply("Python is his favorite language"))
print(p2.apply("I prefer Ruby myself"))
print(p2.apply('We used to use Java'))

# 10.3
p4 = Pattern('cow|pig|horse')
p4.add_response('You had a $1?')
p4.add_response('How many $1s were on the farm?')
print(p4.apply("The horse jumped the fence"))
print(p4.apply("The cow slept in the barn"))
print(p4.apply("The pig wallowed in the sty"))
print()
p5 = Pattern('hamster|guinea pig|gerbil')
p6 = Pattern('I (like|love|adore) my (dog|cat|ducks)')
p6.add_response("Why do you $1 your $2?")
p6.add_response("What about your $2 do you $1?")
print(p6.apply("I adore my cat"))
print(p6.apply("I love my dog"))
print()
p7 = Pattern("I'm afraid of (cows|dogs|ghosts)")
# wild cards : .* : match any piece of text
p = Pattern("I'm afraid of .*")
p.add_response("Why are you afraid of $1?")
print(p.apply("I'm afraid of the dark"))
print(p.apply("I'm afraid of little green men"))
print()
p1 = Pattern("green|yellow|red|blue")
p1.add_response("That’s my favorite color, $1")
print(p1.apply("The sky is red"))
print(p1.apply("The green bird flew away"))
p2 = Pattern("The (dog|cat|frog) (ran|jumped)")
p2.add_response("Are you sure the $1 really $2?")
print(p2.apply("The cat ran away"))
print(p2.apply("The dog jumped over the fence"))
p3 = Pattern("We should .*")
p3.add_response("I don’t want to $1")
print(p3.apply("We should go on a diet"))
print(p3.apply("We should go to the beach tomorrow"))
p4 = Pattern("I’m .* my .* was .*")
p4.add_response("Really, your $2 was $3 made you $1?")
print(p4.apply("I’m totally disappointed my midterm exam was rescheduled"))
p5 = Pattern("I like .*", ["Why do you like $1?"])
print(p5.apply("I like to solve crossword puzzles"))
print(p5.apply("I like your hat"))
print(p5.apply("I like my new computer"))
print()

#10.4
p = Pattern("I am (.*)", ["Are you really $1?"])
pronouns = {"I": "you", "your": "my"}
print(p.apply("I am sorry I dropped your computer", post = pronouns))
print(p.apply("I am happy I lost"))
print(p.apply("I am happy I lost", post = pronouns))
print(p.apply("I’m happy I lost", post = pronouns))
contractions = { "I'm" : "I am" }
print(p.apply("I'm happy I lost", pre = contractions, post = pronouns))
print()
Eliza.load(path_to_data("doctor.txt"))
p = Pattern("You are (.*)", ["I am not $1"])
print(p.apply("You're crazy", pre = Eliza.pre))
print()
p = Pattern("You are (.*)", ["I am not $1"])
print(p.apply("You’re kidding"))
Eliza.load(path_to_data("doctor.txt"))
print(Eliza.pre)
print(Eliza.pre["you're"])
print(Eliza.pre["You're"])
print(p.apply("You're angry", pre = Eliza.pre))
print(p.apply("I hope you're wrong", pre = Eliza.pre))
print(p.apply("She said you are boring", pre = Eliza.pre))
print(p.apply("You're going to laugh at me", Eliza.pre))
print(Eliza.post)
print(p.apply("You're laughing at me", pre = Eliza.pre, post = Eliza.post))
print(p.apply("You are making my point for me", pre = Eliza.pre, post = Eliza.post))
print(p.apply("You are contradicting yourself", pre = Eliza.pre, post = Eliza.post))
print()

# 10.5
print(Eliza.rule_for('remember'))
from PythonLabs.Tools import tokenize
from PythonLabs.ElizaLab import *

def transform(sentence):
    "Generate a response to an input sentence using rules from a script"
    queue = PriorityQueue()
    sentence = Eliza.preprocess(sentence, Eliza.pre)

    for word in tokenize(sentence):
        rule = Eliza.rule_for(word)
        if rule is not None:
            queue.insert(rule)

    while len(queue) > 0:
        rule = queue.pop()
        response = rule.apply(sentence, post = Eliza.post)
        if response is not None:
            return response

    return None

#>>> Eliza.transform("I remember you laughed at me")
#Preprocessing...
#before: 'I remember you laughed at me'
#after: 'I remember you laughed at me'
#Scanning... I*, remember*, you*, laughed, at, me
#Queue: ['remember', 'you', 'i', '$noncommittal']
#Rule for 'remember'
#/\bI remember (.*)/
#Reassembling 'Why do you remember $1 just now?'
#postprocess 'you laughed at me' => 'I laughed at you'
#'Why do you remember I laughed at you just now?'
print()

r = Eliza.rule_for('if')
print(r)
print()
print(r.patterns())
p = r.patterns()[0]
print(p.responses())
Eliza.verbose = True
Eliza.transform('If I could borrow your car')
Eliza.transform('If I remember how to drive')
Eliza.verbose = False
print()

# 10.6
print(path_to_data('doctor.txt'))
print()

# 10.7

# Sum
# Natural Language Processing : The area of computer science research concerned with algorithms for understanding human language
#Turing Test : A proposal for assessing machine intelligence; a program would pass the test if it could carry on a natural language conversation
# ELIZA : The first program to attempt to converse in English; it used simple rules to transform input sentences into responses
# Regular Expressions : A type of expression used for pattern matching; used by the PythonLabs implementation of Eliza to process input sentences
# Semantics : The meaning of a word or sentence; a difficult challenge for natural language processing




