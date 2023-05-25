xs, ys = Hash.new(0), Hash.new(0)
3.times {
    x, y = gets.chomp.split(' ').map(&:to_i)
    xs[x] += 1
    ys[y] += 1
}
puts "#{xs.sort_by {|k, v| v}.to_a[0][0]} #{ys.sort_by {|k, v| v}.to_a[0][0]}"
