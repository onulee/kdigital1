let num = prompt('숫자를 입력하세요.','0');

// num이 짝수이면 짝수입니다. 홀수이면 홀수 입니다. 출력하시오.
// 입력한 값의 7로 나눠서 몫,나머지를 출력하시오.
if(num%2==0)
    document.write('짝수입니다.')
else
    document.write('홀수입니다.')
document.write('<br>')
let result = parseInt(num/7)
document.write(result+'<br>')
let result2 = num%7    
document.write(result2+'<br>')

/*
let num = 15;
if (num>10){
document.write('10보다 큽니다');
document.write('111보다 큽니다');
}
else
document.write('10보다 작습니다.'); 
*/