x, y, z = gets.chomp.split(' ').map(&:to_i)
if y - x == z - y
    puts "cruised"
elsif y - x > 0 && z - y < 0 || y - x < 0 && z - y > 0
    puts "turned"
elsif (y - x).abs > (z - y).abs
    puts "braked"
else
    puts "accelerated"
end