# You may want to pass the signature of a task invocation to another process 
# or as an argument to another function, 
# for which Celery uses something called signatures.

add.signature((2, 2))
add.s(2, 2)


# Signature instances also support the calling API, 
# meaning they have delay and apply_async methods.

s1 = add.s(2, 2)
res = s1.delay()
res.get()
4

# Signatures also supports partial passing of args.

# incomplete partial: add(?, 2)
s2 = add.s(2)

# resolves the partial: add(8, 2)
res = s2.delay(8)
res.get()
10


# Keyword arguments can also be added later
# new arguments taking precedence:

s3 = add.s(2, 2, debug=True)
s3.delay(debug=False)   # debug is now False.
