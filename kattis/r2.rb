input = gets.chomp.split(' ').map(&:to_i)
puts (input[1] - input[0]) + input[1]