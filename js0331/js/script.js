var sum=0;
var arr=[11,2,33,4,55,6,77,8,9,10];
for(var i=0;i<arr.length;i++){ //기본for문
    sum += arr[i];
    document.write(sum);
    document.write('<br>');
}

for(var i in arr){ //향상된for문
    sum += arr[i];
    document.write(sum);
    document.write('<br>');
}
/*
for(var i=0;i<=10;i++){
    sum += i;
    document.write(sum);
    document.write('<br>');
} 
*/



var str1 = '서울인재개발원';
var str2 = '빅데이터 분석가 과정입니다.';
document.write(str1+str2);

let a = 1;
let b = 2;

a = a + b;
a += b;

a = a - b;
a -= b;

a = a * b;
a *= b;

let num = 5;
let num2 = 0;
num2 = ++num;
document.write('num2의 결과값 : '+num2);
document.write('<br>')
document.write('a의 결과값 : '+a)