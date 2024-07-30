def palindrome_config(s: str) -> str:
    s = s.lower()
    # Eliminar caracteres no alfabéticos y espacios
    s = ''.join(char for char in s if char.isalnum())
    return s

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    # Inicializar una tabla 2D para la programación dinámica
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    
    # Cada subcadena de longitud 1 es un palíndromo
    for i in range(n):
        dp[i][i] = True
    
    # Verificar subcadenas de longitud 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2
    
    # Verificar subcadenas de longitud mayor
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_length = length
    
    return s[start:start + max_length]

def map_to_original(original: str, cleaned: str) -> str:
    result = []  # Lista para construir el resultado final
    clean_index = 0  # Índice para recorrer 'cleaned'
    
    for char in original:
        # Verifica si el índice está dentro del rango y si el carácter coincide con el de 'cleaned'
        if clean_index < len(cleaned) and char.lower() == cleaned[clean_index]:
            result.append(char)  # Agrega el carácter actual a 'result'
            clean_index += 1  # Avanza al siguiente carácter en 'cleaned'
        else:
            result.append(' ')  # Agrega un espacio para mantener la estructura original
    
    return ''.join(result)  # Une y devuelve la lista 'result' como una cadena


# Ejemplo de uso
cadena = "Dabale arroz a la zorra el abad"
cleaned_cadena = palindrome_config(cadena)
longest_palindrome_cleaned = longest_palindrome(cleaned_cadena)
resultado_final = map_to_original(cadena, longest_palindrome_cleaned)

print("El palíndromo más largo en la cadena es:", resultado_final)
