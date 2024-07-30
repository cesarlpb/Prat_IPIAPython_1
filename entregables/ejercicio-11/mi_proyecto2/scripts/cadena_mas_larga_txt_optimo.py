def find_repeated_substrings(s):
    # Encontrar cadenas repetidas de manera más eficiente
    seen = {}
    repeated = set()
    for length in range(1, min(len(s), 10)):  # Limitamos la longitud de la subcadena para eficiencia
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring in seen:
                repeated.add(substring)
            seen[substring] = i
    return list(repeated)

def longest_unique_substring(s):
    # Encontrar la cadena más larga sin caracteres repetidos
    char_index = {}
    left = 0
    longest = 0
    start_index = 0
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        if right - left + 1 > longest:
            longest = right - left + 1
            start_index = left
    return s[start_index:start_index + longest]

def main():
    try:
        with open('input.txt', 'r') as file:
            s = file.read().strip()
        
        repeated_substrings = find_repeated_substrings(s)
        longest_unique_substring_result = longest_unique_substring(s)

        print("Cadenas repetidas:")
        print(repeated_substrings)
        print("La cadena más larga sin caracteres repetidos es:")
        print(longest_unique_substring_result)
    except FileNotFoundError:
        print("El archivo 'input.txt' no se encontró.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")

if __name__ == "__main__":
    main()
