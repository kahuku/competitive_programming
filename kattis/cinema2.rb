n = gets.chomp.split(' ').map(&:to_i)[0]
x = gets.chomp.split(' ').map(&:to_i)
s = 0
for i in 0...x.length
    if s + x[i] <= n
        s += x[i]
    else
        break
    end
end
puts x.length - i