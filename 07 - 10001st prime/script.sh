seq 200000 | xargs factor | egrep "[0-9]*: [0-9]*$" | awk '{s+=1; if(s==10001)print $0;}'