# columnvalues.pl
while (<>) {
    @Fields = split /\s+/;
    for $i ( 0 .. $#Fields ) {
        $result[$i]{$Fields[$i]}++
    };
}
for $j ( 0 .. $#result ) {
    print "column $j:\n";
    @values = keys %{$result[$j]};
    @sorted = sort { $result[$j]{$b} <=> $result[$j]{$a}  ||  $a cmp $b } @values;
    for $k ( @sorted ) {
        print " $k $result[$j]{$k}\n"
    }
}
