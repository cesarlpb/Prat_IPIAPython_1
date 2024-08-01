
def compute_prefix_array(pattern):
    """Computa el array de prefijos (tabla de fallos) para el patrón."""
    m = len(pattern)
    prefix_array = [0] * m
    j = 0  # longitud del prefijo más largo

    for i in range(1, m):
        while (j > 0 and pattern[i] != pattern[j]):
            j = prefix_array[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        prefix_array[i] = j

    return prefix_array

def kmp_search(text, pattern):
    """Realiza la búsqueda del patrón en el texto usando el algoritmo KMP."""
    n = len(text)
    m = len(pattern)
    prefix_array = compute_prefix_array(pattern)
    result = []
    j = 0  # índice para el patrón

    for i in range(n):
        while (j > 0 and text[i] != pattern[j]):
            j = prefix_array[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            result.append(i - m + 1)
            j = prefix_array[j - 1]

    return result
