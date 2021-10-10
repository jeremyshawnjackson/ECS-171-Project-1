import json

with open('booksummaries.txt', 'r', encoding="utf8") as summaries, open('summaries.json', 'w', encoding='utf-8') as jsonfile:
  books=[]
  fields = ['title', 'genres', 'book_desc']
  fiction = {'Fantasy', 'Children\'s literature', 'Mystery', 'Young adult literature', 'Suspense', 'Romance novel', 'Adventure novel', 'Alternate history', 'Satire', 'Steampunk'}
  # valid_genres = {'Fiction', 'Science Fiction', 'Fantasy', 'Children\'s literature', 'Mystery', 'Suspense', 'Thriller', 'Horror', 'Romance novel', 'Non-fiction'}
  
  for line in summaries:
    line = line.split('\t')[2:]
    del(line[1:3])

    book = dict(zip(fields, line))

    if (not book['genres'] or not book['book_desc'] or book['book_desc'].startswith('-')):
      continue

    book['book_desc'] = book['book_desc'].strip()

    book['genres'] = [value for key, value in json.loads(book['genres']).items()]
    # book['genres'] = list(set(book['genres']) & valid_genres)

    if 'Non-fiction' in book['genres'] and 'Fiction' in book['genres']:
      book['genres'].pop(book['genres'].index('Fiction'))
    
    # ensure fictional genres are categorized as such
    if bool(set(book['genres']) & fiction):
      book['genres'].append('Fiction')
    
    for key in book['genres']:
      if 'Fiction' in key or ' fiction' in key:
        book['genres'].append('Fiction')
        book['genres'] = list(set(book['genres']))
    
    books.append(book)
  json.dump(books, jsonfile, indent=4)
  