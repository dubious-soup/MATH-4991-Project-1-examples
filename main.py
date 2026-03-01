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

states = {'i1','10','11','12','13','14','15',
          '20','21','22','23','24','25','t1',
          'i2','30','31','32','33','34','35',
          'd0','d1','d2','d3','d4','d5','t2'}
input_alphabet = {'1','2','3','d'}
output_alphabet = input_alphabet
transitions = {'i1':{'e':{('e','10'),('e','20')}},
                '10':{'1':{('1','11'),('2','12'),('3','13')}},
                '11':{'e':{('1','15')}},
                '12':{'1':{('1','15')}},
                '13':{'1':{('1','14')}},
                '14':{'1':{('e','15')}},
                '15':{'e':{('e','t1'),('e','20')}},
                '20':{'2':{('1','21'),('2','22'),('3','23')}},
                '21':{'e':{('2','25')}},
                '22':{'2':{('2','25')}},
                '23':{'2':{('2','24')}},
                '24':{'2':{('e','25')}},
                '25':{'e':{('e','t1'),('e','10')}},
                't1':{'e':{('e','i2')}},
                'i2':{'e':{('e','30'),('e','d0')}},
                '30':{'3':{('1','31'),('2','32'),('3','33')}},
                '31':{'e':{('3','35')}},
                '32':{'3':{('3','35')}},
                '33':{'3':{('3','34')}},
                '34':{'3':{('e','35')}},
                '35':{'e':{('e','t2'),('e','d0')}},
                'd0':{'d':{('1','d1'),('2','d2'),('3','d3')}},
                'd1':{'e':{('d','d5')}},
                'd2':{'d':{('d','d5')}},
                'd3':{'d':{('d','d4')}},
                'd4':{'d':{('e','d5')}},
                'd5':{'e':{('e','t2'),('e','30')}},
                't2':{'e':{('e','i1')}}}
initial_states = {'i1','i2'}
final_states = {'10','20','30','d0'}

audio = FST(states,input_alphabet,output_alphabet,transitions,initial_states,final_states)