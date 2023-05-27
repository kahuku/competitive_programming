text = gets.chomp
l = text.length / 3
if text[0...l] == text[l...2*l] || text[0...l] == text[2*l...]
    puts text[0...l]
else
    puts text[l...2*l]
end