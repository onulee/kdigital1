//구구단 출력
// 2단-9단까지 출력하시오.
// 2*1=2
// 2*2=4
// 2*3=6
// 9*9=81
// 2,4,6,8 -> 짝수단만 출력하시오.

for(let i=2;i<=9;i++){
    if(i%2!=0){
        continue
    }
    for(let j=1;j<=9;j++){
        document.write(i+' * '+j+' = '+(i*j)+'<br>');
    }
}

// let input =10;
// let i=0
// let sum=0
// // 홀수 : 빨강, 짝수는 파랑으로 1-10출력을 해보세요.

// for(i=1;i<=10;i++){
//     if(i%2==0)
//     document.write('<p class="a2">'+i+'</p>');
//     else
//     document.write('<p class="a1">'+i+'</p>');
// }

// document.write(sum)
