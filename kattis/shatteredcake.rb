w = gets.chomp.to_i
n = gets.chomp.to_i
area = 0

n.times do
  area += gets.chomp.split.map(&:to_i).reduce(:*)
end

puts (area / w).to_i