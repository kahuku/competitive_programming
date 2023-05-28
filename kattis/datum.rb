require 'date'
day, month = gets.chomp.split(' ').map(&:to_i)
date = Date.new(2009, month, day)
case date.cwday
when 1
    puts 'Monday'
when 2 
    puts 'Tuesday'
when 3
    puts 'Wednesday'
when 4
    puts 'Thursday'
when 5
    puts 'Friday'
when 6
    puts 'Saturday'
when 7
    puts 'Sunday'
end
