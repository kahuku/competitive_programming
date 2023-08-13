#!/bin/ruby

require 'json'
require 'stringio'

# Too slow
# Goldman Sachs 2023 intern application

#
# Complete the 'countPalindromes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromes(s, ws)
    count = 0
    for i in 0...(s.length() - ws + 1)
        s2 = s[i, ws]
        if s2 == s2.reverse
            count += 1
        end
    end
    count
end

def countPalindromes(s)
    count = s.length()
    for i in 2...(s.length() + 1)
        count += palindromes(s, i)
    end
    count
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

s = gets.chomp

result = countPalindromes s

fptr.write result
fptr.write "\n"

fptr.close()
