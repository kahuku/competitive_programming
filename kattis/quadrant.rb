x = gets.to_i
y = gets.to_i
if x > 0 and y > 0
    puts 1
elsif x < 0 and y > 0
    puts 2
elsif x < 0 and y < 0
    puts 3
else
    puts 4
end