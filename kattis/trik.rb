a, b, c = true, false, false
gets.chomp.each_char { |ch|
    if ch == 'A'
        a,b = b,a
    elsif ch == 'B'
        b,c = c,b
    else
        a,c = c,a
    end
}
x = if a then 1 elsif b then 2 else 3 end
puts x