const header =document.querySelector('header')
window.addEventListener("scroll", (e) => {
    // console.log(this.scrollY
    if (this.scrollY > 100) {
        header.classList.add("sticky");
    } else if (this.scrollY == 0) {
        
        header.classList.remove("sticky");
    }

    
})