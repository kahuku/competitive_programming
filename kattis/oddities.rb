for _ in 0...gets.chomp.to_i do
    n = gets.chomp.to_i
    puts "#{n} is #{n % 2 == 0 ? "even" : "odd"}"
end