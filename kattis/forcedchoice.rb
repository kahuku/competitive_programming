require 'set'
n_cards, choice, rounds = gets.chomp.split(' ').map(&:to_i)
for _ in 0...rounds do
   cards =  gets.chomp.split(' ').map(&:to_i)[1..].to_set
   puts (cards.include? choice) ? "KEEP" : "REMOVE"
end