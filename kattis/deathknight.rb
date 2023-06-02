n = gets.to_i
c = (1..n).count { !gets.include?("CD") }
puts c