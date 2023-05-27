gets; l = gets.chomp.split(' ').map(&:to_i).sort
s = l[0]
for i in 1...l.length do
    s += l[i] if l[i] != l[i - 1] + 1
end
puts s

# solution 2
gets
l = gets.chomp.split(' ').map(&:to_i).sort
s = l.slice_when { |a, b| b != a + 1 }.map(&:first).sum
puts s