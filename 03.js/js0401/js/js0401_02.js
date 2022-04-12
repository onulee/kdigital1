let a = 17;
let b = 19;
let c = 18;

//삼항식
//let result = (a>b)?a:b;
//document.write(a+','+b+' 중에 더 큰수는 ?'+result+'<br>');
//document.write('<hr>');
//삼항식
//let result = (a>b)? ((a>c)?a:c) : ((b>c)?b:c);
//document.write(a+','+b+','+c+' 중에 더 큰수는 ?'+result+'<br>');
//document.write('<hr>');

let re2 = Math.max(a,b,c);
document.write(a+','+b+' 중에 더 큰수는 ?'+re2+'<br>');

let result1=''
if(a>b){
    result1='a가 더 큽니다.'
}else{
    result1='b가 더 큽니다.'
}
document.write(result1+'<br>');


let sum = 0;
for(let i=1;i<=10;i++){
    sum += i ;
}
document.write('sum의 값 : '+sum);







