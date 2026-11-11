# this is a program that shows an example of a brute-force attack program 
# this is an example of a phone password generator of 6 digtis

from string import digits 

for i in digits: 
  for j in digits:
    for k in digits: 
      for l in digits:
        for m in digits:
          for n in digits:
            print(i, j, k, l, m, n)



# for 4 digits you can remove the m and n in digits 
# incase you want a letter guessing program 
# use ascii_letters in the import and in part 

# BIG BIG reminder, please use this at your own risk and don't use it to harm other
# these are for educational purpose only
