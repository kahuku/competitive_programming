n = gets.chomp.to_i
s = 0
for _ in 0...n do
    s += gets.chomp.to_i
end
puts s - n + 1

# solution 2

n = gets.chomp.to_i
s = n.times.map { gets.chomp.to_i }.sum
puts s - n + 1