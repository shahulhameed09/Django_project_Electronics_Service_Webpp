let menu = document.querySelector('#menu-btn');
let navbarLinks = document.querySelector('.header .navbar .links');

menu.onclick = () =>{
   menu.classList.toggle('fa-times');
   navbarLinks.classList.toggle('active');
}

function validateform(){
    const re=/[0-9]{10}/;
    var e = document.getElementsByClassName('phone').value;

    if (re.test(e)) {
        document.getElementsByClassName('formerror').value='in';
    }
    else{
        document.getElementsByClassName('formerror').value='*Enter valid phone number';
    }
}
