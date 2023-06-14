
#!/usr/bin/env python3

#open connection to nc challenges.404ctf.fr

import pwn

host = "challenges.404ctf.fr"
port = 31420



def count_occurence(data):
    count = 0
    for i in data:
        if i == 0x7e:
            count += 1
    return count

# open connection and received input using pwn
conn = pwn.remote(host, port)
data = conn.recvline()
print(data)
data = conn.recvline()
print(data)

# count total number of occurence
total = 0
while True:
    data = conn.recvline()
    print(data)
    total += count_occurence(data)
    print(total)

    if "Votre" in str(data):
        conn.sendline(str(total))
        print("sending total")
        total = 0

# goto interactive
conn.interactive()
