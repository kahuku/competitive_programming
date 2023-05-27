input = gets.chomp.split(' ').map(&:to_i)
problems, cases = input[0], input[1]
solves = 0
problems.times do
    passes = 0
    cases.times do
        word = gets.chomp
        passes += 1 if word[1..-1] == word[1..-1].downcase
    end
    solves += 1 if passes == cases
end
puts solves