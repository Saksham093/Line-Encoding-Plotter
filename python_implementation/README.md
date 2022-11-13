# Improvement in Code and Design.
----

There was en error, because user inconfused with the input. SO, I changed that and also added the condition of correct input value type of signal and encoding type.


### Condition for the Input of the Signal...
```
while True:
    signal = str(input('Input Signal to be Plotted (1s and 0s) : '))
    ls = map(lambda x: x in {'0', '1'}, signal)

    if False in ls:
        print("\nInvalid Input Try Again.\n")
        continue
    
    break
```

### To avoid Error if Encoding not in the list...
```

print('\nEncode in Format:\n1. NRZ-I\n2. NRZ-L\n3. RZ\n4. Manchester\n5. Diff Manchester ...\n')
while True:
    encoding = str(input("\nEnter Int Value from the List : "))
    if encoding not in ['1', '2', '3', '4', '5']:
        print("\nInvalid Input Type...Retry")
        continue

    break
```

----
