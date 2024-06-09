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

    // Enabling/Disabling answers and changing background for benefits 
    var tittle = document.getElementsByClassName("tittle");
    var i = 0;
    for (i = 0; i < tittle.length; i++) {
        console.log(tittle[i])

        tittle[i].addEventListener("click", function () {
            this.firstElementChild.classList.toggle("fa-chevron-down")
            this.firstElementChild.classList.toggle("fa-chevron-up")
            this.classList.toggle("active")

            var desc = this.nextElementSibling;
            if (desc.style.display === "block") {
                    desc.style.display = "none";
            } else {
                    desc.style.display = "block";
            }
        }
        )
    }

    document.querySelectorAll('.fa-heart').forEach(item => {
        item.addEventListener('click', function() {
            const recid = this.id;

            fetch(`/toggle_favourite/${recid}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify({'in_favourite': this.classList.contains('added_in_fav')})
            })        
            .then(res => {
                if(res.ok) {
                    return res.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then(data => {
                if(data.new_in_favourite)
                    this.classList.add('added_in_fav')
                else
                    this.classList.remove('added_in_fav')
            })

            if(this.classList.contains('far')) {
                this.classList.remove('far');
                this.classList.add('fas');
                this.style.color = 'red';
            } else {
                this.classList.remove('fas');
                this.classList.add('far');
                this.style.color = '';
            }
        });
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