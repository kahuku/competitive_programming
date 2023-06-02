gets; x = gets.chomp.split.map(&:to_i)
puts x.reduce(0, :+) % 3 == 0 ? "yes" : "no"