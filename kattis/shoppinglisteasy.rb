require 'set'
n = gets.chomp.split.map(&:to_i)[0]
s = Set.new(gets.chomp.split)
for i in 1...n do
    s = s & Set.new(gets.chomp.split)
end
s = s.to_a.sort
puts s.length
for i in 0...s.length do
    puts s[i]
end