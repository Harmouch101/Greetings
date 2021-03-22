import sys, base64, sqlite3
# Create a databse called greetings.
conn = sqlite3.connect('greetings.db')
c = conn.cursor()
# Create a table called greetings.
c.execute('CREATE TABLE greetings ([msg] text)')
conn.commit()
# Decode a base64 hello world message. 
msg = base64.b64decode(b'SGVsbG8gV29ybGQgCg==').decode('ascii')
c.execute("INSERT INTO greetings VALUES(?)", (msg,))
conn.commit()
# Select 
c.execute("SELECT msg FROM greetings")
# Fetch all records.
words = c.fetchall()[0][0]
# Override the print method.
print = lambda word: sys.stdout.write(word)
# Lazly fetch words
def fetch_word(msg):
  yield from msg.split()
# print Hello World.
for word in fetch_word(words):
  _ = print(word + ' ')