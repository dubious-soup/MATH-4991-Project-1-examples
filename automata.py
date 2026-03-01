from itertools import chain
from collections import deque

#Finite State Automata
class FSA:
    def __init__(self, states, alphabet, transitions, initial_states, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_states = initial_states
        self.final_states = final_states

    def __str__(self):
        adjacency_table = ""
        for state, transition in self.transitions.items():
            for symbol, new_states in transition.items():
                adjacency_table += f"\n{state} -({symbol})> {new_states}"
        return adjacency_table
    
    def validate_path(self, string, state):
        if len(string) == 0:
            if state in self.final_states:
                return True
            else:
                return False
        
        if (string[0] in self.transitions[state]):
            for new_state in self.transitions[state][string[0]]:
                if self.validate_path(string[1:],new_state):
                    return True
        else:
            return False


    def accept(self, string):
        for initial_state in self.initial_states:
            if self.validate_path(string, initial_state):
                return True
        return False

#Finite State Transducer
class FST:

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_states, final_states):
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_states = initial_states
        self.final_states = final_states

    def __str__(self):
        adjacency_table = ""
        for state, transition in self.transitions.items():
            for symbol, new_states in transition.items():
                for new_state in new_states:
                    adjacency_table += f"\n{state} -({symbol}|{new_state[0]})> {new_state[1]}"
        return adjacency_table
    
    def translate_path(self, string, state):
        e_new_translated_ends = set()
        new_translated_ends = set()

        if ('e' in self.transitions[state]):
            for new_state in self.transitions[state]['e']:
                translated_ends = self.translate_path(string,new_state[1])
                for translated_end in translated_ends:
                    translated_end = deque(list(translated_end))
                    translated_end.appendleft(new_state[0])
                    e_new_translated_ends.add(tuple(translated_end))
        else:
            if len(string) == 0:
                if state in self.final_states:
                    return {('e',)}
                else:
                    return set()
        
        if len(string) == 0:
            return e_new_translated_ends

        if (string[0] in self.transitions[state]):
            for new_state in self.transitions[state][string[0]]:
                translated_ends = self.translate_path(string[1:],new_state[1])
                for translated_end in translated_ends:
                    translated_end = deque(list(translated_end))
                    translated_end.appendleft(new_state[0])
                    new_translated_ends.add(tuple(translated_end))
        return e_new_translated_ends|new_translated_ends

    def validate_path(self, string, state):
        if len(string) == 0:
            if state in self.final_states:
                return True
            else:
                return False
        
        if (string[0] in self.transitions[state]):
            for new_state in self.transitions[state][string[0]]:
                if self.validate_path(string[1:],new_state[1]):
                    return True
        else:
            return False

    @staticmethod
    def remove_empty_symbols(messy_set, is_str):
        cleaned_set = set()
        for string in messy_set:
            string = [symbol for symbol in list(string) if symbol != 'e']
            if is_str:
                string = "".join(string)
            else:
                string = tuple(string)
            cleaned_set.add(string)
        return cleaned_set

    def accept(self, string, is_str = False):
        if is_str:
            string = list(string)
        translations = set()
        for initial_state in self.initial_states:
            translations = translations|self.translate_path(string, initial_state)
        return self.remove_empty_symbols(translations, is_str)

        