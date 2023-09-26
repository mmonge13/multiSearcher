import subprocess

# Término de búsqueda
search_query = input('Ingrese el término de búsqueda: ')

# Diccionario con nombres de navegadores y sus ubicaciones en el sistema
browsers = {
    # Ejemplo de ubicación de Chrome en Windows
    'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    # Ejemplo de ubicación de Edge en Windows
    'msedge': r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    # Ejemplo de ubicación de Firefox en Windows
    'firefox': r'C:\Program Files\Mozilla Firefox\firefox.exe',
    # Puedes agregar más navegadores y sus ubicaciones aquí
}

# Intenta abrir cada navegador con los resultados de la búsqueda
for browser, path in browsers.items():
    print(f'Buscando "{search_query}" en {browser}...')

    try:
        subprocess.Popen(
            [path, f'https://www.google.com/search?q={search_query}'])
    except FileNotFoundError:
        print(
            f'{browser} no se encontró en tu sistema o la ubicación del navegador es incorrecta.')

# Si deseas, puedes agregar más navegadores y ubicaciones a la lista 'browsers'
