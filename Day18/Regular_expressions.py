#Exercices: Level 1
#1 (The most frequent word in the following paragraph)
import re
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'
print(Counter(re.findall(r"\w+", paragraph, re.I)))

#2 (The distance between the two furthest particles)
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles'
point = re.findall(r'-?\d+', txt)
print(point)
point_int = list(map(int, point))
print(point_int)
dst = max(point_int) - min(point_int)
print(dst)

#Exercices: Level 2
def is_valid_variable(name):
    pattern = r'^[a-zA-Z_]\w*$'
    return bool(re.match(pattern, name))

print(is_valid_variable("for"))

#Exercices: Level 3
sentences = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
sub_sentences = re.sub(r"[@#%&$]", "", sentences)
print(sub_sentences)

from collections import Counter
compteur = Counter(re.findall(r"\w+", sub_sentences, re.I))
print(compteur.most_common(3))