function fetchchange(){
    fetch('/fetchChange').then(response=>response.json()).then(
        function(data){
            // console.log(typeof(data))
            if(data.sensor1=='0'){
                var s1=document.getElementById('s1-status')
                // console.log(typeof(s1))
                s1.innerText='PARKED'
                s1.style.backgroundColor='crimson';
            }
            else{
                var s1=document.getElementById('s1-status')
                s1.innerText='FREE'
                s1.style.backgroundColor='green';
            }
            if(data.sensor2=='0'){
                var s2=document.getElementById('s2-status')
                s2.innerText='PARKED'
                s2.style.backgroundColor='crimson';
            }
            else{
                var s2=document.getElementById('s2-status')
                s2.innerText='FREE'
                s2.style.backgroundColor='green';
            }
            if(data.sensor3=='0'){
                var s3=document.getElementById('s3-status')
                s3.innerText='PARKED'
                s3.style.backgroundColor='crimson';
            }
            else{
                var s3=document.getElementById('s3-status')
                s3.innerText='FREE'
                s3.style.backgroundColor='green';
            }
            if(data.sensor4=='0'){
                var s4=document.getElementById('s4-status')
                s4.innerText='PARKED'
                s4.style.backgroundColor='crimson';
            }
            else{
                var s4=document.getElementById('s4-status')
                s4.innerText='FREE'
                s4.style.backgroundColor='green';
            }
    })
}
var s1=document.getElementById('s1-status')
      
var s3=document.getElementById('s3-status')
var s4=document.getElementById('s4-status')
                
setInterval(fetchchange, 5000);