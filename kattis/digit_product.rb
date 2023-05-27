num = gets.chomp
while num.length() > 1 do
    new_num = 1
    num.each_char { |digit|
        digit = digit.to_i
        if digit != 0
            new_num *= digit
        end
    }
    num = new_num.to_s
end
puts num