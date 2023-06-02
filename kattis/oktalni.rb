d = {
    '000' => '0',
    '001' => '1',
    '010' => '2',
    '011' => '3',
    '100' => '4',
    '101' => '5',
    '110' => '6',
    '111' => '7'
}

b = gets.chomp
if b.length % 3 == 1
    b = '00' + b
elsif b.length % 3 == 2
    b = '0' + b
end
o = ''
for i in (0...b.length).step(3) do
    o += d[b[i...i+3]]
end
puts o