function filterCars() {
    const searchInput = document.getElementById('search').value.toLowerCase();
    const cars = document.querySelectorAll('.car');

    cars.forEach(car => {
        const carName = car.getAttribute('data-name').toLowerCase();
        if (carName.includes(searchInput)) {
            car.style.display = 'block';
        } else {
            car.style.display = 'none';
        }
    });
}
