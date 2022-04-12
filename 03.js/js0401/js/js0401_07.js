let site = prompt('원하는 번호를 클릭하세요.\n 1.네이버 2.다음 3.구글');
document.write(site);


switch(site){
    case '1': case'5':case '6': 
    case '4':
        alert('네이버를 선택했습니다.');
        location.href='http://www.naver.com';
        break;
    case '2':
        alert('다음을 선택했습니다.');
        location.href='http://www.daum.net';
    break;
    case '3':
        alert('구글을 선택했습니다.');
        location.href='http://www.google.com'
    break;
    default:
        alert('잘못선택하셨습니다.');
    break;
}


if(site==1 || site>5){

}else if(site==2){

}else{

}