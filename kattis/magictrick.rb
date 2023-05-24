require 'set'
s = gets.chomp
se = Set[]
s.each_char { |c|
    if se.include? c
        puts 0
        exit
    end
    se.add(c)
}
puts 1