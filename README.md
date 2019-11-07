# cross-platform-RSA
Python, Android(JAVA) Use RSA Sample. Python(server) encrypt, Android(Client) decrypt
by using PKCS1Padding!!!

# Logic
Client(aos) creates Key-Pair, public-key and private-key. We can share the public-key to encrypt a plain text. But, decrypt only the client(who has private-key) can do. 

So, create key-pair and send the public-key to server. Server, Save the Key and encrypt some text, and send to client the encrypted message. Client, can decrypt that.



# blog (kor)
https://cholol.tistory.com/472
