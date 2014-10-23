#!/usr/bin/python

import hyperdex.admin
a = hyperdex.admin.Admin('127.0.0.1', 1982)
import hyperdex.client
c = hyperdex.client.Client('127.0.0.1', 1982)

a.rm_space('friendlists')

a.add_space('''space friendlists
key username
attributes
   string first,
   string last,
   set(string) friends
''')

c.put('friendlists', 'jsmith1', {'first': 'John', 'last': 'Smith', 'friends': set(['bjones1', 'jd', 'jj'])})
c.put('friendlists', 'jd', {'first': 'John', 'last': 'Doe'})
c.put('friendlists', 'bjones1', {'first': 'Brian', 'last': 'Jones'})

print(c.get('friendlists', 'jsmith1'))

print(c.cond_put('friendlists', 'jsmith1', {'first': 'John', 'last': 'Smith'}, {'first': 'Jon'}))

print(c.get('friendlists', 'jsmith1'))

print(c.cond_put('friendlists', 'jsmith1', {'first': 'John', 'last': 'Smith'}, {'first': 'Jon'}))

