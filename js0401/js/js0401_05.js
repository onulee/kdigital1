//입력받은 점수가 
// 90점이상이면 A
// 80점이상이면 B
// 70점이상이면 C
// 60점이상이면 D
// 60점 미만 F

let score = prompt('점수를 입력하세요.','0')

if(score>=90)
    document.write('A학점')
else if(score>=80)
    document.write('B학점')
else if(score>=70)
    document.write('C학점')
else if(score>=60)
    document.write('D학점')
else
    document.write('F학점')