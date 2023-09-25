# Define the sets of search operators
operator_sets = {
    "Search Operators": [
        '"" exact',
        '- exclusion',
        '* wildcard',
        'AROUND(n) around'
    ],
    "Date Operators": [
        'yyyy-mm-dd',
        'after: yyyy-mm-dd',
        'before: yyyy-mm-dd',
        'yyyy..yyyy'
    ],
    "Source Operators": [
        'site/search:',
        'ext/filetype:',
        'source:',
        'loc/location:',
        'Blogurl:',
        'Cache:'
    ],
    "Boolean Operators": [
        'and',
        'or'
    ],
    "In Operators": [
        'inurl/allinurl:',
        'intitle/allintitle:',
        'intext/allIntext:',
        'inanchor/allinanchor:'
    ],
    "Utility Operators": [
        'Define',
        'Related',
        'Ip address',
        'x un Y',
        '$ xx .. yy',
        '@',
        'Weather:',
        'Map:',
        'Movie:',
        'Stock:'
    ]
}

# Define a dictionary to map operators to their processing functions
operator_processors = {
    '"" exact': lambda query: f'"{query}"',
    '- exclusion': lambda query: f'-{query}',
    '* wildcard': lambda query: f'*{query}',
    'AROUND(n) around': lambda query: f'AROUND(n){query}',
    'yyyy-mm-dd': lambda query: f'daterange:{query}',
    'after: yyyy-mm-dd': lambda query: f'after:{query}',
    'before: yyyy-mm-dd': lambda query: f'before:{query}',
    'yyyy..yyyy': lambda query: f'daterange:{query}',
    'site/search:': lambda query: f'site:{query}',
    'ext/filetype:': lambda query: f'filetype:{query}',
    'source:': lambda query: f'source:{query}',
    'loc/location:': lambda query: f'location:{query}',
    'Blogurl:': lambda query: f'blogurl:{query}',
    'Cache:': lambda query: f'cache:{query}',
    'and': lambda query: f'{query} AND',
    'or': lambda query: f'{query} OR',
    'inurl/allinurl:': lambda query: f'inurl:{query}',
    'intitle/allintitle:': lambda query: f'intitle:{query}',
    'intext/allIntext:': lambda query: f'intext:{query}',
    'inanchor/allinanchor:': lambda query: f'inanchor:{query}',
    'Define': lambda query: f'define:{query}',
    'Related': lambda query: f'related:{query}',
    'Ip address': lambda query: f'ip:{query}',
    'x un Y': lambda query: f'{query} X {query}',
    '$ xx .. yy': lambda query: f'${query}',
    '@': lambda query: f'@{query}',
    'Weather:': lambda query: f'weather:{query}',
    'Map:': lambda query: f'map:{query}',
    'Movie:': lambda query: f'movie:{query}',
    'Stock:': lambda query: f'stock:{query}',
}