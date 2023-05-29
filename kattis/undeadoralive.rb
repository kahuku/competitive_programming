s = gets.chomp
if s.include?(":)") && s.include?(":(")
  puts "double agent"
elsif !s.include?(":)") && s.include?(":(")
  puts "undead"
elsif s.include?(":)") && !s.include?(":(")
  puts "alive"
else
  puts "machine"
end