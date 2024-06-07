window.onload = function () {
    console.log("website is loaded!!");
    const header = document.querySelector('header');
    const hamburger_menu_btn = document.querySelector(".hamburger");
    const mobile_nav = document.querySelector(".mobile-nav");

    // Enable/Disable header backgroud 
    window.addEventListener('scroll', function (e) {
        if (window.pageYOffset > 100) {
            header.classList.add('is-scrolling');
        } else {
            header.classList.remove('is-scrolling');
        }
    });

    // Enable/Disable mobile nav menu
    hamburger_menu_btn.addEventListener("click", function () {
        console.log("clicked");
        hamburger_menu_btn.classList.toggle("is-active");
        mobile_nav.classList.toggle("is-active");
    });

    // Function to update the left position
    // Call the function initially and whenever the window is resized
    window.addEventListener('resize', function () {
        const screenWidth = window.innerWidth;
        // Remove classes based on the screen width
        if (screenWidth > 1024) {
            hamburger_menu_btn.classList.remove("is-active");
            mobile_nav.classList.remove("is-active");
        }
    });


}

function showTab(tabNumber) {
    const tabs = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');

    tabs.forEach((tab, index) => {
        if (index + 1 === tabNumber) {
            tab.classList.add('active');
            tabContents[index].style.display = 'block';
        } else {
            tab.classList.remove('active');
            tabContents[index].style.display = 'none';
        }
    });
}