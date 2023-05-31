r, c = gets.chomp.split(' ').map(&:to_f)
puts (100 * ((r - c) ** 2) / (r ** 2))