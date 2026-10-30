
document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("productSearch");
    const filterButtons = document.querySelectorAll(".filter-btn");
    const productCards = document.querySelectorAll(".product-card");
    const noResults = document.getElementById("noResults");

    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    let selectedCategory = "All";

    function filterProducts() {

        const searchTerm = searchInput.value.toLowerCase().trim();
        let visibleCount = 0;

        productCards.forEach(function (card) {

            const category = card.dataset.category;
            const name = card.dataset.name;

            const matchesCategory =
                selectedCategory === "All" ||
                category === selectedCategory;

            const matchesSearch = name.includes(searchTerm);

            if (matchesCategory && matchesSearch) {
                card.style.display = "";
                visibleCount++;
            } else {
                card.style.display = "none";
            }

        });

        noResults.style.display =
            visibleCount === 0 ? "block" : "none";
    }

    filterButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            selectedCategory = button.dataset.filter;

            filterButtons.forEach(function (item) {
                item.classList.remove("active");
            });

            button.classList.add("active");

            filterProducts();
        });

    });

    searchInput.addEventListener("input", filterProducts);

    document.querySelectorAll(".category-card").forEach(function (card) {

        card.addEventListener("click", function () {

            selectedCategory = card.dataset.category;

            filterButtons.forEach(function (button) {

                button.classList.toggle(
                    "active",
                    button.dataset.filter === selectedCategory
                );

            });

            filterProducts();

        });

    });

    menuToggle.addEventListener("click", function () {
        navLinks.classList.toggle("open");
    });

    navLinks.querySelectorAll("a").forEach(function (link) {

        link.addEventListener("click", function () {
            navLinks.classList.remove("open");
        });

    });

});
