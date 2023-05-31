line_number = 1
while line = STDIN.gets
    x = line.split.map(&:to_i)[1..-1]
    puts "Case #{line_number}: #{x.min} #{x.max} #{x.max - x.min}"
    line_number += 1
end