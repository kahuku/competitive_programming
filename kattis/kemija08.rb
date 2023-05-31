inp = gets.chomp
vowels = ['a', 'e', 'i', 'o', 'u']
i = 0
s = ''
while i < inp.length
    s += inp[i]
    if vowels.include?(inp[i])
        i += 3
    else
        i += 1
    end
end
puts s