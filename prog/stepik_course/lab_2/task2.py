def int2base(x, base):
  digs = "0123456789abcdefghijklmnopqrstuvwxyz"
  if x == 0: return digs[0]

  digits = []

  while x:
    digits.append(digs[int(x % base)])
    # x = int(x / base)
    x = x // base

  return ''.join(reversed(digits))

def convert(num, count):
  diff = count - len(num)

  if diff > 0:
    for _ in range(diff):
      num.insert(0, "0")

  return "".join(num)

if __name__ == "__main__":
  inputs = input().split(" ")

  assoc_table = {"0": "A", "1": "C", "2": "G", "3": "T"}
  print(*[assoc_table[j] for j in convert(list(int2base(int(inputs[0]), len(assoc_table))), int(inputs[1]))], sep='')
