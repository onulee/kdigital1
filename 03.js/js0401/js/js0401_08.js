let sum=0;
// let input= prompt('숫자를 입력하세요.','0');
let input=10;
let i=0;

// 홀수는 글자색 빨강, 짝수는 파랑
//
while(i<input){
    i++;
    //홀수 그냥
    //짝수 *
    if(i%2==0)
    document.write('<p class="a2">'+i+'</p>');
    else
    document.write('<p class="a1">'+i+'</p>');
}





//원하는 수까지 합계를 구하려면
// 2의 배수, 5의배수는 제외후 합계를 구하시오. - continue

// while(i<input){
//     i++;
//     if(i%2==0 || i%5==0)  continue
//     sum += i;
// }

// document.write(sum);