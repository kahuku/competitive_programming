l, r = gets.chomp.split(' ').map(&:to_i)
puts l == r && r == 0 ? "Not a moose" : "#{l == r ? "Even" : "Odd"} #{2 * [l, r].max}"