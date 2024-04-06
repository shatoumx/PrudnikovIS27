# Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

text = '--msg-template="$FileDir${path}:{line}:{column}:{C}:({symbol}){msg}"'

punct = [symbol for symbol in text if symbol in string.punctuation]

print("Punctuation symbols in the string:", punct)