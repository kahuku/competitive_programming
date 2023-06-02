n = gets.chomp.to_i
c = 0
for i in 0...n do
    s = gets.chomp.downcase
    if s.include?("rose") || s.include?("pink")
        c += 1
    end
end
puts c > 0 ? c : "I must watch Star Wars with my daughter"