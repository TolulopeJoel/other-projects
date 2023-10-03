print('generate code for texts')  # text coder
plain_text = input('kindly write your text here// ').lower()
plain_text_separated = list(plain_text)
plain_text_separated.reverse()
code_generator_dictionary = {
    'q': '1', 'b': ']',
    'w': '2', 'g': '#',
    'e': '3', 'n': ')',
    'r': '4', ',': '-',
    't': '5', '.': '*',
    'y': '6',
    'u': '7',
    'i': '8',
    'o': '9',
    'p': '0',
}
output = ''
for texts in plain_text_separated:
    output += code_generator_dictionary.get(texts, texts)
print(f'>> {output}')
try:
    with open('coded_texts.txt', 'x') as coded_output_text:
        new_texts = coded_output_text.write(output)
except FileExistsError:
    with open('coded_texts.txt', 'a') as coded_output_text:
        new_texts = coded_output_text.writelines(f'\n\n{output}')

print('\ndecode coded texts')  # text decoder
coded_text = input('kindly write your text here// ').lower()
coded_text_separated = list(coded_text)
coded_text_separated.reverse()
decode_generator_dictionary = {
    '1': 'q', ']': 'b',
    '2': 'w', '#': 'g',
    '3': 'e', ')': 'n',
    '4': 'r', '-': ',',
    '5': 't', '*': '.',
    '6': 'y',
    '7': 'u',
    '8': 'i',
    '9': 'o',
    '0': 'p'
}
output = ''
for codes in coded_text_separated:
    output += decode_generator_dictionary.get(codes, codes)
print(f'>> {output}')
try:
    with open('decoded_texts.txt', 'x') as decoded_output_text:
        new_texts = decoded_output_text.write(output)
except FileExistsError:
    with open('decoded_texts.txt', 'a') as decoded_output_text:
        new_texts = decoded_output_text.writelines(f'\n\n{output}')
