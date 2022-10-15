const countdown = () => {
    const countdate = new Date('March 1, 2024 00:00:00').getTime();
    const currentDate = new Date().getTime();
    const diff= countdate - currentDate;
console.log(diff);

    const seconds = 1000;
    const minutes = seconds * 60;
    const hours = minutes * 60;
    const days = hours * 24;
    const months = days * 30;
    const years = months * 12;

    const textyear = Math.floor(diff / years) ;
   const textmonth = Math.floor((diff % years) / months) ;
   const textdays = Math.floor((diff % months) / days) ;
   const texthours = Math.floor((diff % days) / hours) ;   
   const textminutes = Math.floor((diff % hours) / minutes) ;    
   const textseconds = Math.floor((diff % minutes) / seconds) ;   

   document.querySelector('.years').innerText = textyear ; 
   document.querySelector('.months').innerText = textmonth ; 
   document.querySelector('.days').innerText = textdays ; 
   document.querySelector('.hours').innerText = texthours ; 
   document.querySelector('.mins').innerText = textminutes ; 
   document.querySelector('.secs').innerText = textseconds ; 

} 

setInterval(countdown, 1000);