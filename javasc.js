///Clickable opening button of vartical navbar
const menubtn = document.querySelector("#menu-btn");
const vertnavbar = document.querySelector("#v-navbar");

menubtn.addEventListener('click',()=>{
    console.log("'clicked'");
    vertnavbar.style.display='flex';
})    

//Clickable Closing button of vertical navbar
const closebtn = document.querySelector("#close-btn");
  
closebtn.addEventListener('click',()=>{
    vertnavbar.style.display='none';
})