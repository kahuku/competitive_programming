# this doesn't work
time, tasks = gets.chomp.split(' ').map(&:to_i)[1], gets.chomp.split(' ').map(&:to_i)
used, i = 0, 0
loop do
    used += tasks[i]
    break if used >= time
    i += 1
    break if i == tasks.length()
end
puts i