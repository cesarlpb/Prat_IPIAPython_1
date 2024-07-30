def find_repeated_substrings(s):
    # Encontrar cadenas repetidas
    seen = {}
    repeated = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring in seen:
                if seen[substring] == 1:
                    repeated.append(substring)
                seen[substring] += 1
            else:
                seen[substring] = 1
    repeated = list(set(repeated))  # Eliminar duplicados en la lista de repetidos
    return repeated

def longest_unique_substring(s):
    # Encontrar la cadena más larga sin caracteres repetidos
    char_set = set()
    left = 0
    longest = 0
    start_index = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > longest:
            longest = right - left + 1
            start_index = left
    return s[start_index:start_index + longest]

def main():
    s = input("Ingresa una cadena de caracteres: ")

    repeated_substrings = find_repeated_substrings(s)
    longest_unique_substring_result = longest_unique_substring(s)

    print("Cadenas repetidas:")
    print(repeated_substrings)
    print("La cadena más larga sin caracteres repetidos es:")
    print(longest_unique_substring_result)

if __name__ == "__main__":
    main()
    # Ingresa una cadena de caracteres: 123asdf123/1234
    # Cadenas repetidas:
    # ['1', '2', '3', '12', '123', '23']
    # La cadena más larga sin caracteres repetidos es:
    # asdf123/