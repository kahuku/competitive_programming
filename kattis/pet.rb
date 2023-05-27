scores = []
for _ in 0...5 do
    scores << gets.chomp.split(' ').map(&:to_i).sum
end
puts "#{scores.rindex(scores.max) + 1} #{scores.max}"