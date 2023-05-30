gets; inp = gets.chomp
stack = []
opening_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']
bracket_pairs = { ')' => '(', ']' => '[', '}' => '{' }
inp.each_char do |char|
    if opening_brackets.include?(char)
        stack.push(char)
    elsif closing_brackets.include?(char)
        if stack.empty? || stack.pop != bracket_pairs[char]
            puts 'Invalid'
            exit
        end
    end
end
puts stack.empty? ? "Valid" : "Invalid"