a = 'Single quote'
b = "Double quote"
c = '''
  Triple qu
  ote
'''

print(a)
print(b)
print(c)

print('i' in a)
print(f"letter 'i' is in a: {'i' in a}")


symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
print(f"symbols={symbols}")
print(f"symbols[0]={symbols[0]}")
print(f"symbols[-2]={symbols[-2]}")

symbols = symbols + ',GOOG'
print(f"new symbols={symbols}")

print(f"IBM is in symbols: {'IBM' in symbols}")
