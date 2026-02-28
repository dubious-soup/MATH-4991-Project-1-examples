from automata import FSA
from automata import FST

states = {'s0','s1'}
alphabet = {'a','b'}
transitions = {'s0':{'a':{'s0'},'b':{'s1'}},
                's1':{'a':{'s1'},'b':{'s1'}}}
initial_states = {'s0'}
final_states = {'s1'}

my_automata = FSA(states,alphabet,transitions,initial_states,final_states)

states = {'s0','s1','s2','s3','s4','s5'}
input_alphabet = {'a'}
output_alphabet = {'a','1','2','3'}
transitions = {'s0':{'a':{('1','s1'),('2','s2'),('3','s3')}},
                's1':{'e':{('a','s5')}},
                's2':{'a':{('a','s5')}},
                's3':{'a':{('a','s4')}},
                's4':{'a':{('e','s5')}},
                's5':{}}
initial_states = {'s0'}
final_states = {'s5'}

bounded_a_counter = FST(states,input_alphabet,output_alphabet,transitions,initial_states,final_states)

print(bounded_a_counter)
print(bounded_a_counter.accept('a', is_str = True))