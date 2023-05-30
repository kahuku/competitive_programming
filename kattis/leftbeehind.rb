a, b = gets.chomp.split(' ').map(&:to_i)
while a != 0 || b != 0 do
    if a + b == 13
        puts 'Never speak again.'
    elsif a == b
        puts 'Undecided.'
    elsif a > b
        puts 'To the convention.'
    else
        puts 'Left beehind.'
    end
    a, b = gets.chomp.split(' ').map(&:to_i)
end