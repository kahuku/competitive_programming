n = gets.chomp.to_i
for i in 0...n do
    s = gets.chomp
    if s == 'P=NP'
        puts "skipped"
    else
        s = s.split('+').map(&:to_i)
        puts s[0] + s[1]
    end
end