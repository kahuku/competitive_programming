n, k, p = gets.chomp.split(' ').map(&:to_f)
puts n * p - k >= 0 ? 'spela inte!' : 'spela'