var userHeight = prompt('키를 입력하세요.','0');
let userWeight = prompt('몸무게를 입력하세요.','0');

// 평균 체중 = (키 - 100)*0.9
let normal_w = (userHeight-100)*0.9;
document.write('평균체중 : '+normal_w+'<br>');
document.write('본인체중 : '+userWeight+'<br>');

if(normal_w>userWeight){
    document.write('평균체중보다 작습니다.');
}else if(normal_w==userWeight){
    document.write('평균체중입니다.');
}else{
    document.write('평균체중보다 높습니다.');
}
