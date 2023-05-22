time, tasks = gets.chomp.split(' ').map(&:to_i)[1], gets.chomp.split(' ').map(&:to_i)
used, count = 0, 0
for i in 0...tasks.length
    used += tasks[i]
    if used > time
        break
    end
    count += 1
end
puts count