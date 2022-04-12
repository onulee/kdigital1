let name1 = prompt('이름을 입력하세요.','');
document.write(typeof(name1)+'<br>');
let age = prompt('나이를 입력하세요.','');
document.write(typeof(age)+'<br>');

if(age>18){
    document.write('성인입니다.');
}else{
    document.write('미성년자입니다.');
}

