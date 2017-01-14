ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
       6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
ones2 = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
          16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
start = {0: 'and', 100: 'hundred', 1000: 'onethousand'}

len1_9 = 0
len10_19 = 0
len20_99 = 0

for a in range(1,10):
    len1_9 += len(ones[a])

for a in range(10,20):
    len10_19 += len(ones2[a])

for a in range(2,10):
    len20_99 = len20_99 + len(tens[a]) * 10 + len1_9

len1_99 = len1_9 + len10_19 + len20_99
len100_999 = len1_9 * 100 + len1_99 * 9 + len(start[100]) * 9 + 9 * 99 * (len(start[100] + start[0]))

h = len1_99 + len100_999 + len(start[1000])
print(h)