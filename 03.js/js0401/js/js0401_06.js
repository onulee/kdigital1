// id,pw를 확인하는 프로그램구현

let count=0;

    alert(count)
    let id = prompt('아이디를 입력하세요.');
    let pw = prompt('패스워드를 입력하세요.');
    if (id=='admin')
        if(pw=='1111'){
            document.write('아이디와 패스워드 일치')
            location.href='http://www.naver.com' //페이지 이동
        }
        else{
           document.write('패스워드가 일치하지 않음.')
           alert('패스워드가 일치하지 않습니다. 다시 입력하세요.')
           location.reload() //f5 새로고침
        }
    else{
        document.write('아이디가 일치하지 않음') 
        alert('아이디가 일치하지 않습니다. 다시 입력하세요.') 
        location.reload()       
    }
